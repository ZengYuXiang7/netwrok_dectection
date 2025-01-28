# coding : utf-8
# Author : yuxiang Zeng

import torch
import numpy as np
from scapy.utils import rdpcap
from sklearn.preprocessing import MinMaxScaler

from baselines.graph_baselines import build_single_graph
from baselines.statistics import get_flow_feature
from datasets.pcap.protocol_raw.protocol import get_protocol, get_all_mapping
from utils.config import get_config
from utils.logger import Logger
from utils.plotter import MetricsPlotter
from utils.utils import set_settings
from tqdm import *
import os
import pandas as pd
import pickle

class experiment:
    def __init__(self, config):
        self.config = config

    def load_data(self, config):
        # 定义文件路径
        interval_path = f'./datasets/flow/{config.dataset}_all_interval_{config.flow_length_limit}'
        seq_path = f'./datasets/flow/{config.dataset}_all_seq_{config.flow_length_limit}'
        labels_path = f'./datasets/flow/{config.dataset}_all_labels_{config.flow_length_limit}'
        if config.model == 'stat':
            interval_path += 'stat.pickle'
            seq_path += 'stat.pickle'
            labels_path += 'stat.pickle'
        else:
            interval_path += '.pickle'
            seq_path += '.pickle'
            labels_path += '.pickle'

        # 检查文件是否存在
        if os.path.exists(interval_path) and os.path.exists(seq_path) and os.path.exists(labels_path):
            # 如果文件存在，加载数据
            all_interval = pickle.load(open(interval_path, 'rb'))
            all_seq = pickle.load(open(seq_path, 'rb'))
            all_labels = pickle.load(open(labels_path, 'rb'))
        else:
            from flowcontainer.extractor import extract
            from utils.config import get_config
            all_flow = os.listdir(f'./datasets/pcap/{config.dataset}')
            all_interval, all_seq, all_labels = [], [], []
            if config.dataset == 'protocol':
                mapping = get_all_mapping()
            for i in trange(len(all_flow)):
                add = f'./datasets/pcap/{config.dataset}/' + os.listdir(f'./datasets/pcap/{config.dataset}')[i]
                if '.pcapng' in add:
                    continue
                result = extract(add, filter='(tcp or udp)')
                print(add, len(result))
                for key in result:
                    value = result[key]
                    if len(value.ip_timestamps) < config.flow_length_limit:
                        continue
                    time_stamp = value.ip_timestamps[:config.flow_length_limit]
                    if config.model == 'stat':
                        seq = get_flow_feature(value)
                    else:
                        seq = value.ip_lengths[:config.flow_length_limit]
                    # interval = np.diff(time_stamp)
                    # interval = np.insert(interval, 0, 0)
                    all_interval.append(time_stamp)
                    all_seq.append(seq)
                    if config.dataset == 'protocol':
                        # print(add.split('/')[-1])
                        # print(mapping)
                        label = mapping[add.split('/')[-1]]
                        all_labels.append(label)
                        # all_labels.append(i)
                        # exit()
                    else:
                        all_labels.append(i)
                # print('label:', label)
            all_interval = np.stack(all_interval)
            all_interval /= np.max(all_interval)
            all_seq = np.stack(all_seq)
            pickle.dump(all_interval, open(interval_path, 'wb'))
            pickle.dump(all_seq, open(seq_path, 'wb'))
            pickle.dump(all_labels, open(labels_path, 'wb'))
        all_info = {
            'max_flow_length': config.flow_length_limit,
            'max_packet_length': np.max(all_seq),
            'num_classes': np.max(all_labels) + 1,
        }
        all_labels = np.array(all_labels)
        pickle.dump(all_info, open(f'./datasets/flow/{config.dataset}_info_{config.flow_length_limit}.pickle', 'wb'))
        # 初始化 MinMaxScaler
        if config.model == 'stat':
            scaler = MinMaxScaler()
            all_seq = scaler.fit_transform(all_seq)
        print(np.max(all_interval), all_seq.max(), all_seq.min())
        print(all_seq.shape, all_labels.shape)
        # exit()
        if config.model == 'stat':
            all_x = all_seq.astype(np.float32)
        else:
            all_x = np.concatenate([all_interval, all_seq], axis=-1).astype(np.float32)

        all_y = all_labels
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
            TensorDataset(train_x, train_y, 'train', config),
            TensorDataset(valid_x, valid_y, 'valid', config),
            TensorDataset(test_x, test_y, 'test', config)
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
            random.shuffle(now_x)
            train_size = int(len(now_x) * config.density)
            valid_size = int(len(now_x) * 0.10) if config.eval_set else 0
            train_x.extend(now_x[:train_size])  # 同时保存 five 和 flow
            train_y.extend([label] * len(now_x[:train_size]))
            valid_x.extend(now_x[train_size:train_size + valid_size])
            valid_y.extend([label] * len(now_x[train_size:train_size + valid_size]))
            test_x.extend(now_x[train_size + valid_size:])
            test_y.extend([label] * len(now_x[train_size + valid_size:]))
        # train_x, train_y, valid_x, valid_y, test_x, test_y = map(np.array, [train_x, train_y, valid_x, valid_y, test_x, test_y])
        max_value = 1
        return train_x, train_y, valid_x, valid_y, test_x, test_y, max_value


class TensorDataset(torch.utils.data.Dataset):
    def __init__(self, x, y, mode, config):
        self.config = config
        self.x = x
        self.y = y
        self.mode = mode
        dataset_info = pickle.load(open(f'./datasets/flow/{config.dataset}_info_{config.flow_length_limit}.pickle', 'rb'))
        self.max_packet_length = dataset_info['max_packet_length']
        self.max_flow_length = dataset_info['max_flow_length']
        if self.config.model in ['gnn', 'dapp', 'graphiot']:
            address = f'./datasets/flow/{config.dataset}_{config.flow_length_limit}_{self.mode}_graph.pickle'
            # if self.config.model == 'graphiot':
            #     address = f'./datasets/flow/{config.dataset}_{config.flow_length_limit}_{self.mode}_graphiot.pickle'
            try:
                with open(address, 'rb') as f:
                    self.all_graph = pickle.load(f)
            except Exception as e:
                print(e)
                self.all_graph = []
                for i in trange(len(x)):
                    seq_input = self.x[i]
                    seq_input = torch.tensor(seq_input)
                    time_interval = seq_input[:self.config.flow_length_limit]
                    seq_input = seq_input[self.config.flow_length_limit:]
                    seq_input /= self.max_packet_length
                    graph = build_single_graph(seq_input, time_interval, self.config)
                    self.all_graph.append(graph)
                with open(address, 'wb') as f:
                    pickle.dump(self.all_graph, f)

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        raw_input = self.x[idx]
        raw_input = torch.tensor(raw_input)
        time_interval = raw_input[:self.config.flow_length_limit]
        seq_input = raw_input[self.config.flow_length_limit:]
        seq_input /=  self.max_packet_length
        if self.config.model in ['gnn', 'dapp', 'graphiot']:
            time_interval = self.all_graph[idx]
            seq_input = torch.as_tensor([1.0])
        elif self.config.model == 'stat':
            time_interval = torch.as_tensor([1.0])
            seq_input = raw_input

        label = self.y[idx]
        return time_interval, seq_input, label


import dgl
def custom_collate_fn(batch, config):
    from torch.utils.data.dataloader import default_collate
    time_interval, seq_input, labels = zip(*batch)
    if config.model in ['gnn', 'dapp', 'graphiot']:
        time_interval = dgl.batch(time_interval)
    else:
        time_interval = default_collate(time_interval)
    seq_input = default_collate(seq_input)
    label = torch.as_tensor(labels, dtype=torch.long if config.classification else torch.float32)
    return time_interval, seq_input, label


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
