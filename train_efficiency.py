# coding : utf-8
# Author : yuxiang Zeng


def calculate_flops_params(model, sample_input, config):
    from thop import profile
    sample_input = tuple([item.to(config.device) for item in sample_input][:-1])
    flops, params = profile(model.to(config.device), inputs=sample_input, verbose=False)
    # config.log.only_print(f"Flops: {flops} Params: {params}")
    return flops, params


def calculate_inference_time(model, sample_input, config):
    from time import time
    import numpy as np
    step = 100
    all_time = []
    for i in range(step):
        a, b, _ = tuple([item.to(config.device) for item in sample_input])
        t1 = time()
        model(a, b)
        t2 = time()
        all_time.append(t2 - t1)
    inference_time = np.mean(all_time)
    # config.log.only_print(f"Average Inference Time: {inference_time * 1000:.2f} ms")
    return inference_time * 1000


def only_run():
    # Experiment Settings, logger, plotter
    from utils.config import get_config
    from utils.logger import Logger
    from utils.plotter import MetricsPlotter
    from utils.utils import set_settings, set_seed
    from train_model import Model

    config = get_config()
    set_settings(config)
    log_filename = f'Model_{config.model}_{config.dataset}_S{config.train_size}_R{config.rank}_Ablation{config.Ablation}'
    plotter = MetricsPlotter(log_filename, config)
    log = Logger(log_filename, plotter, config)

    from data import experiment, DataModule

    exper = experiment(config)
    datamodule = DataModule(exper, config)
    model = Model(datamodule, config).to(config.device)

    sample_inputs = next(iter(datamodule.train_loader))
    flops, params = calculate_flops_params(model, sample_inputs, config)
    inference_time = calculate_inference_time(model, sample_inputs, config)
    # estimate_gpu_memory(model, sample_inputs, config)
    return flops, params, inference_time


def get_efficiency(config):
    from train_model import Model
    from data import experiment, DataModule
    exper = experiment(config)
    datamodule = DataModule(exper, config)
    model = Model(datamodule, config)
    sample_inputs = next(iter(datamodule.train_loader))
    flops, params = calculate_flops_params(model, sample_inputs, config)
    inference_time = calculate_inference_time(model, sample_inputs, config)
    # estimate_gpu_memory(model, sample_inputs, config)
    return flops, params, inference_time


if __name__ == '__main__':
    only_run()
