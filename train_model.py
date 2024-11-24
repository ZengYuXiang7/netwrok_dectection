# coding : utf-8
# Author : yuxiang Zeng
import collections
import time

import numpy as np
import pandas as pd
import torch
import pickle
import sys
import os
from tqdm import *
from train_efficiency import get_efficiency
from utils.metrics import ErrorMetrics
from utils.monitor import EarlyStopping
from utils.trainer import get_loss_function, get_optimizer
from utils.utils import makedir, set_seed
from torchvision import models

global log, config
torch.set_default_dtype(torch.float32)


class Predictor(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(Predictor, self).__init__()
        self.NeuCF = torch.nn.Sequential(
            torch.nn.Linear(input_dim, hidden_dim // 2),  # FFN
            torch.nn.LayerNorm(hidden_dim // 2),  # LayerNorm
            torch.nn.ReLU(),  # ReLU
            torch.nn.Linear(hidden_dim // 2, hidden_dim // 2),  # FFN
            torch.nn.LayerNorm(hidden_dim // 2),  # LayerNorm
            torch.nn.ReLU(),  # ReLU
            torch.nn.Linear(hidden_dim // 2, output_dim)  # y
        )

    def forward(self, x):
        y = self.NeuCF(x)
        return y


class Model(torch.nn.Module):
    def __init__(self, input_size, config):
        super().__init__()
        self.config = config
        self.input_size = input_size
        self.hidden_size = config.rank
        self.pretrain = True

        if config.model == 'ours':
            input_dim = 1024
            weights = models.DenseNet121_Weights.IMAGENET1K_V1 if self.pretrain else None
            self.encoder = models.densenet121(weights=weights)
            self.encoder.classifier = torch.nn.Linear(input_dim, self.hidden_size)
        else:
            raise ValueError(f"Unsupported model type: {config.model}")

        self.predictor = Predictor(self.hidden_size, config.rank, 5)

    def forward(self, x):
        hidden = self.encoder(x)
        y = self.predictor(hidden)
        return y

    def setup_optimizer(self, args):
        self.to(args.device)
        self.loss_function = get_loss_function(args).to(args.device)
        self.optimizer = get_optimizer(self.parameters(), lr=args.lr, decay=args.decay, args=args)
        self.scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(self.optimizer, mode='min' if args.classification else 'max', factor=0.5, patience=args.patience // 1.5, threshold=0.0)

    def train_one_epoch(self, dataModule):
        loss = None
        self.train()
        torch.set_grad_enabled(True)
        t1 = time.time()
        for train_Batch in (dataModule.train_loader):
            # 这个写法能够直接免掉右边的一切，左边复制好就行
            image_tensor, label = tuple(item.to(self.config.device) for item in train_Batch)
            pred = self.forward(image_tensor)
            loss = self.loss_function(pred, label)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
        t2 = time.time()
        self.eval()
        torch.set_grad_enabled(False)
        return loss, t2 - t1

    def evaluate_one_epoch(self, dataModule, mode='valid'):
        self.eval()
        torch.set_grad_enabled(False)
        dataloader = dataModule.valid_loader if mode == 'valid' and len(dataModule.valid_loader.dataset) != 0 else dataModule.test_loader
        val_loss = 0.
        preds = []
        reals = []

        for batch in (dataloader):
            image_tensor, label = tuple(item.to(self.config.device) for item in batch)
            pred = self.forward(image_tensor)
            if mode == 'valid':
                val_loss += self.loss_function(pred, label)
            if self.config.classification:
                pred = torch.max(pred, 1)[1]  # 获取预测的类别标签
            preds.append(pred)
            reals.append(label)
        reals = torch.cat(reals, dim=0)
        preds = torch.cat(preds, dim=0)
        if mode == 'valid':
            self.scheduler.step(val_loss)
        metrics_error = ErrorMetrics(reals * dataModule.max_value, preds * dataModule.max_value, self.config)
        return metrics_error



def RunOnce(config, runId, log):
    # Set seed
    set_seed(config.seed + runId)

    # Initialize
    from data import experiment, DataModule
    exper = experiment(config)
    datamodule = DataModule(exper, config)
    model = Model(datamodule, config)
    # model.compile()

    # Setting
    monitor = EarlyStopping(config)
    makedir(f'./checkpoints/{config.model}')
    model_path = f'./checkpoints/{config.model}/{log.filename}_round_{runId}.pt'

    # Check if retrain is required or if model file exists
    retrain_required = config.retrain == 1 or not os.path.exists(model_path)

    if not retrain_required:
        try:
            model.load_state_dict(torch.load(model_path, weights_only=True, map_location='cpu'))
            model.setup_optimizer(config)
            results = model.evaluate_one_epoch(datamodule, 'test')
            sum_time = pickle.load(open(f'./results/metrics/' + log.filename + '.pkl', 'rb'))['train_time'][runId]
            if not config.classification:
                log(f'MAE={results["MAE"]:.4f} RMSE={results["RMSE"]:.4f} NMAE={results["NMAE"]:.4f} NRMSE={results["NRMSE"]:.4f}')
            else:
                log(f'Acc={results["Acc"]:.4f} F1={results["F1"]:.4f} Precision={results["P"]:.4f} Recall={results["Recall"]:.4f}')
            config.record = False
        except Exception as e:
            log.only_print(f'Error: {str(e)}')
            retrain_required = True
            print()

    if retrain_required:
        model.setup_optimizer(config)
        train_time = []
        for epoch in trange(config.epochs):
            if monitor.early_stop:
                break
            epoch_loss, time_cost = model.train_one_epoch(datamodule)
            valid_error = model.evaluate_one_epoch(datamodule, 'valid')
            monitor.track_one_epoch(epoch, model, valid_error, 'NRMSE' if not config.classification else 'Acc')
            log.show_epoch_error(runId, epoch, monitor, epoch_loss, valid_error, train_time)
            train_time.append(time_cost)
            log.plotter.append_epochs(valid_error)
        model.load_state_dict(monitor.best_model)
        sum_time = sum(train_time[: monitor.best_epoch])
        results = model.evaluate_one_epoch(datamodule, 'test')
        log.show_test_error(runId, monitor, results, sum_time)
        torch.save(monitor.best_model, model_path)
        log.only_print(f'Model parameters saved to {model_path}')
    results['train_time'] = sum_time
    return results


def RunExperiments(log, config):
    log('*' * 20 + 'Experiment Start' + '*' * 20)
    metrics = collections.defaultdict(list)

    for runId in range(config.rounds):
        log.plotter.reset_round()
        try:
            results = RunOnce(config, runId, log)
            for key in results:
                metrics[key].append(results[key])
            log.plotter.append_round()
        except Exception as e:
            raise Exception
            log(f'Run {runId + 1} Error: {e}, This run will be skipped.')
        except KeyboardInterrupt:
            break

    log('*' * 20 + 'Experiment Results:' + '*' * 20)
    for key in metrics:
        log(f'{key}: {np.mean(metrics[key]):.4f} ± {np.std(metrics[key]):.4f}')
    # flops, params, inference_time = get_efficiency(config)
    # log(f"Flops: {flops:.0f}")
    # log(f"Params: {params:.0f}")
    # log(f"Inference time: {inference_time:.2f} ms")
    if config.record:
        log.save_result(metrics)
        log.plotter.record_metric(metrics)
    log('*' * 20 + 'Experiment Success' + '*' * 20)
    return metrics


def run(config):
    from utils.logger import Logger
    from utils.plotter import MetricsPlotter
    from utils.utils import set_settings, set_seed
    set_settings(config)
    log_filename = f'Model_{config.model}_Dataset_{config.dataset}_D{config.density:.3f}_R{config.rank}'
    plotter = MetricsPlotter(log_filename, config)
    log = Logger(log_filename, plotter, config)
    try:
        metrics = RunExperiments(log, config)
        # log.send_email(log_filename, metrics, 'zengyuxiang@hnu.edu.cn')
        log.end_the_experiment()
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(error_details)
        # log.send_email(log_filename, error_details, 'zengyuxiang@hnu.edu.cn')
        sys.exit(1)  # 终止程序，并返回一个非零的退出状态码，表示程序出错

    return metrics

if __name__ == '__main__':
    # Experiment Settings, logger, plotter
    from utils.config import get_config
    config = get_config()
    run(config)
