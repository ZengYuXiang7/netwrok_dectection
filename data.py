# coding : utf-8
# Author : yuxiang Zeng

import torch
import numpy as np
from sphinx.builders.gettext import timestamp

from utils.config import get_config
from utils.logger import Logger
from utils.plotter import MetricsPlotter
from utils.utils import set_settings

from torch.nn.utils.rnn import pad_sequence

from tqdm import *
from data_generator import csv_to_flow
import os
import pandas as pd
import pickle

class experiment:
    def __init__(self, config):
        self.config = config

    @staticmethod
    def load_data(config):
        def get_all_flow(dataset):
            try:
                all_data = pickle.load(open(f'./datasets/flow/{dataset}.pickle', 'rb'))
            except Exception as e:
                datasets_path = os.path.join('./datasets', 'csv', dataset)
                all_files = os.listdir(datasets_path)
                all_csv_data = []
                for i in range(len(all_files)):
                    df = pd.read_csv(os.path.join(datasets_path, all_files[i]))
                    all_csv_data.append(df)
                all_data = []
                time_interval = 10
                for i in trange(len(all_csv_data)):
                    all_data.append(csv_to_flow(all_csv_data[i], time_interval))
                os.makedirs('./datasets/flow')
                pickle.dump(all_data, open(f'./datasets/flow/{dataset}.pickle', 'wb'))
            return all_data
        try:
            all_x = pickle.load(open(f'./datasets/flow/{config.dataset}_all_x.pickle', 'rb'))
            all_y = pickle.load(open(f'./datasets/flow/{config.dataset}_all_y.pickle', 'rb'))
            dataset_info = pickle.load(open(f'./datasets/flow/{config.dataset}_info.pickle', 'rb'))
        except Exception as e:
            print(e)
            all_data = get_all_flow(config.dataset)
            all_x, all_y = [], []
            for i in range(len(all_data)):
                for key, value in tqdm(all_data[i].items()):
                    this_flow = []
                    for item in value:
                        this_flow.append([item[0], item[-1]])
                    # 统计数据到达 90 % 的流事件长度为 1320
                    if len(this_flow) > 1320 or len(this_flow) == 0:
                        # print(len(this_flow))
                        # exit()
                        continue
                    all_x.append(this_flow)
                    all_y.append(i)
            pickle.dump(all_x, open(f'./datasets/flow/{config.dataset}_all_x.pickle', 'wb'))
            pickle.dump(all_y, open(f'./datasets/flow/{config.dataset}_all_y.pickle', 'wb'))

            max_packet_length = 0
            max_flow_length = 0
            for i in range(len(all_x)):
                max_flow_length = max(max_flow_length, len(all_x[i]))
                for j in range(len(all_x[i])):
                    max_packet_length = max(max_packet_length, abs(all_x[i][j][1]))
            # print(max_flow_length, max_packet_length)
            dataset_info = {
                'max_flow_length': max_flow_length,  # padding使用
                'max_packet_length': max_packet_length,  # 包序列归一化
                'num_classes': max(all_y) + 1,
            }
            pickle.dump(dataset_info, open(f'./datasets/flow/{config.dataset}_info.pickle', 'wb'))

        return all_x, all_y


    def get_pytorch_index(self, data):
        return torch.as_tensor(data)


# 数据集定义
class DataModule:
    def __init__(self, exper_type, config):
        self.config = config
        self.path = config.path
        self.x, self.y = exper_type.load_data(config)
        if config.debug:
            self.x, self.y = self.x[:300], self.y[:300]
        self.train_x, self.train_y, self.valid_x, self.valid_y, self.test_x, self.test_y, self.max_value = (
            self.get_train_valid_test_dataset(self.x, self.y, config)) if not config.classification else self.get_train_valid_test_classification_dataset(self.x, self.y, config)
        self.train_set, self.valid_set, self.test_set = self.get_dataset(self.train_x, self.train_y, self.valid_x, self.valid_y, self.test_x, self.test_y, config)
        self.train_loader, self.valid_loader, self.test_loader = get_dataloaders(self.train_set, self.valid_set, self.test_set, config)
        config.log.only_print(f'Train_length : {len(self.train_loader.dataset)} Valid_length : {len(self.valid_loader.dataset)} Test_length : {len(self.test_loader.dataset)} Max_value : {self.max_value:.2f}')

    def get_dataset(self, train_x, train_y, valid_x, valid_y, test_x, test_y, config):
        return (
            TensorDataset(train_x, train_y, config),
            TensorDataset(valid_x, valid_y, config),
            TensorDataset(test_x, test_y, config)
        )

    def preprocess_data(self, x, y, config):

        return x, y

    def get_train_valid_test_dataset(self, x, y, config):
        x, y = self.preprocess_data(x, y, config)
        indices = np.random.permutation(len(x))
        x, y = x[indices], y[indices]

        if not config.classification:
            max_value = y.max()
            y /= max_value
        else:
            max_value = 1

        train_size = int(len(x) * config.density)
        if config.eval_set:
            valid_size = int(len(x) * 0.10)
        else:
            valid_size = 0

        train_x = x[:train_size]
        train_y = y[:train_size]

        valid_x = x[train_size:train_size + valid_size]
        valid_y = y[train_size:train_size + valid_size]

        test_x = x[train_size + valid_size:]
        test_y = y[train_size + valid_size:]

        return train_x, train_y, valid_x, valid_y, test_x, test_y, max_value


    def get_train_valid_test_classification_dataset(self, x, y, config):
        x, y = self.preprocess_data(x, y, config)
        from collections import defaultdict
        import random
        class_data = defaultdict(list)
        for now_x, now_label in zip(x, y):
            class_data[now_label].append(now_x)
        train_x, train_y = [], []
        valid_x, valid_y = [], []
        test_x, test_y = [], []
        for label, now_x in class_data.items():
            flow = now_x
            random.shuffle(flow)
            train_size = int(len(flow) * config.density)
            valid_size = int(len(flow) * 0.10) if config.eval_set else 0
            train_x.extend(flow[:train_size])  # 同时保存 five 和 flow
            train_y.extend([label] * train_size)
            valid_x.extend(flow[train_size:train_size + valid_size])
            valid_y.extend([label] * valid_size)
            test_x.extend(flow[train_size + valid_size:])
            test_y.extend([label] * (len(flow) - train_size - valid_size))
        # train_x, train_y, valid_x, valid_y, test_x, test_y = map(np.array, [train_x, train_y, valid_x, valid_y, test_x, test_y])
        max_value = 1
        return train_x, train_y, valid_x, valid_y, test_x, test_y, max_value


class TensorDataset(torch.utils.data.Dataset):
    def __init__(self, all_x, all_y, config):
        self.config = config
        self.all_x = all_x
        self.all_y = all_y
        dataset_info = pickle.load(open(f'./datasets/flow/{config.dataset}_info.pickle', 'rb'))
        self.max_packet_length = dataset_info['max_packet_length']
        self.max_flow_length = dataset_info['max_flow_length']


    def __len__(self):
        return len(self.all_x)

    def __getitem__(self, idx):
        seq_input = self.all_x[idx]
        # 手动归一化 1514
        seq_input = torch.tensor(seq_input)
        stamp = seq_input[:, 0]
        seq = seq_input[:, 1] / self.max_packet_length

        # 0 Padding，注意这里是否合理，所以需要一个实验检验的过程
        times_stamp = torch.zeros(self.max_flow_length, dtype=stamp.dtype)
        times_stamp[:stamp.shape[0]] = stamp

        seq_input = torch.zeros(self.max_flow_length, dtype=seq.dtype)
        seq_input[:seq.shape[0]] = seq

        label = self.all_y[idx]
        return times_stamp, seq_input, label


def custom_collate_fn(batch, config):
    from torch.utils.data.dataloader import default_collate
    times_stamp, seq_input, labels = zip(*batch)
    times_stamp = default_collate(times_stamp)
    seq_input = default_collate(seq_input)
    label = torch.as_tensor(labels, dtype=torch.long if config.classification else torch.float32)
    return times_stamp, seq_input, label


def get_dataloaders(train_set, valid_set, test_set, config):
    import platform
    from torch.utils.data import DataLoader
    import multiprocessing
    if platform.system() == 'Linux' and 'ubuntu' in platform.version().lower():
        max_workers = multiprocessing.cpu_count() // 5
        prefetch_factor = 4
    else:
        max_workers = 0
        prefetch_factor = None

    train_loader = DataLoader(
        train_set,
        batch_size=config.bs,
        drop_last=False,
        shuffle=True,
        pin_memory=True,
        collate_fn=lambda batch: custom_collate_fn(batch, config),
        num_workers=max_workers,
        prefetch_factor=prefetch_factor
    )
    valid_loader = DataLoader(
        valid_set,
        batch_size=config.bs,
        drop_last=False,
        shuffle=False,
        pin_memory=True,
        collate_fn=lambda batch: custom_collate_fn(batch, config),
        num_workers=max_workers,
        prefetch_factor=prefetch_factor
    )
    test_loader = DataLoader(
        test_set,
        batch_size=config.bs,
        drop_last=False,
        shuffle=False,
        pin_memory=True,
        collate_fn=lambda batch: custom_collate_fn(batch, config),
        num_workers=max_workers,
        prefetch_factor=prefetch_factor
    )

    return train_loader, valid_loader, test_loader


if __name__ == '__main__':

    config = get_config()
    set_settings(config)
    config.experiment = True

    # logger plotter
    exper_detail = f"Dataset : {config.dataset.upper()}, Model : {config.model}, Train_size : {config.train_size}"
    log_filename = f'{config.train_size}_r{config.rank}'
    log = Logger(log_filename, exper_detail, config)
    plotter = MetricsPlotter(log_filename, config)
    config.log = log
    log(str(config.__dict__))


    exper = experiment(config)
    datamodule = DataModule(exper, config)
    for train_batch in datamodule.train_loader:
        num_windowss, value = train_batch
        print(num_windowss.shape, value.shape)
        # break
    print('Done!')
