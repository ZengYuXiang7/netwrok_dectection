# coding : utf-8
# Author : yuxiang Zeng

import torch
import numpy as np
from sphinx.builders.gettext import timestamp

from data_preprocess.csv_to_flow import get_all_input
from utils.config import get_config
from utils.logger import Logger
from utils.plotter import MetricsPlotter
from utils.utils import set_settings


from torch.nn.utils.rnn import pad_sequence

class experiment:
    def __init__(self, config):
        self.config = config

    @staticmethod
    def load_data(config):
        dataset_labels = {
            'bashlite_leg': 0,
            'mirai_leg': 0,
            'torii_leg': 0,
            'bashlite_mal_spread_all': 1,
            'bashlite_mal_CC_all': 2,
            'mirai_mal_spread_all': 3,
            'mirai_mal_CC_all': 4,
            'torii_mal_all': 5,
        }
        y = []
        all_five_tuple, all_seq = [], []
        for dataset, item in dataset_labels.items():
            now_five_tuple, now_seq, now_labels = get_all_input(dataset, config.time_interval, dataset_labels[dataset])
            # print(len(now_five_tuple), len(now_seq))
            # exit()
            all_five_tuple += now_five_tuple
            all_seq += now_seq
            y += list(now_labels)
        x = [all_five_tuple, all_seq]
        return x, y



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
        all_five_tuple, all_seq = x

        # 将 all_five_tuple 转换为 NumPy 数组
        all_five_tuple = np.array(all_five_tuple)
        print(all_five_tuple)

        # 确保输入是二维数组
        if all_five_tuple.ndim != 2 or all_five_tuple.shape[1] != 5:
            raise ValueError("all_five_tuple 应该是一个二维数组，形状为 (n_samples, 5)")

        # 初始化 LabelEncoders
        from sklearn.preprocessing import LabelEncoder
        label_encoder_ip = LabelEncoder()  # 第一列和第二列共享
        label_encoder_port = LabelEncoder()
        label_encoder_protocol = LabelEncoder()

        # 分别对每一列进行编码
        col1_and_col2 = np.concatenate((all_five_tuple[:, 0], all_five_tuple[:, 1]))  # 合并第一列和第二列
        col1_and_col2_encoded = label_encoder_ip.fit_transform(col1_and_col2)  # 对合并的列编码

        # 第一列和第二列的编码结果
        col1_encoded = col1_and_col2_encoded[:len(all_five_tuple)]
        col2_encoded = col1_and_col2_encoded[len(all_five_tuple):]

        # 第三列（source_port）编码
        col3_encoded = label_encoder_port.fit_transform(all_five_tuple[:, 2])

        # 第四列（destination_port）编码
        col4_encoded = label_encoder_port.fit_transform(all_five_tuple[:, 3])

        # 第五列（protocol）编码
        col5_encoded = label_encoder_protocol.fit_transform(all_five_tuple[:, 4])

        # 将编码后的列合并回一个二维数组
        all_five_tuple_encoded = np.column_stack([col1_encoded, col2_encoded, col3_encoded, col4_encoded, col5_encoded])

        # 查看结果
        print("原始五元组：", all_five_tuple[:5])  # 显示前 5 个五元组
        print("编码后的五元组：", all_five_tuple_encoded[:5])  # 显示前 5 个编码结果

        # 对序列做归一化
        max_value = 0.0
        max_length = 0
        print(max(all_seq))
        for i in range(len(all_seq)):
            max_length = max(max_length, len(all_seq[i]))
            for j in range(len(all_seq[i])):
                # print(all_seq[i][j][1])
                max_value = max(all_seq[i][j][1], max_value)
        for i in range(len(all_seq)):
            for j in range(len(all_seq[i])):
                # print(all_seq[i][j])
                all_seq[i][j][1] /= max_value
                # print(all_seq[i][j])
        print(max(all_seq), max_length)
        config.max_length = max_length
        x = all_five_tuple_encoded, all_seq
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
        class_data = defaultdict(list)
        for now_x, now_label in zip(x, y):
            class_data[now_label].append(now_x)
        train_x, train_y = [], []
        valid_x, valid_y = [], []
        test_x, test_y = [], []
        for label, now_x in class_data.items():
            # indices = np.random.permutation(len(x))
            # x, y = x[indices], y[indices]

            five_tuple, seq = now_x
            # 对 x（five_tuple 和 seq）同时打乱
            indices = np.random.permutation(len(five_tuple))  # 生成随机索引
            five_tuple = five_tuple[indices]
            seq = [seq[i] for i in indices]

            # 划分训练集、验证集和测试集
            train_size = int(len(five_tuple) * config.density)
            valid_size = int(len(five_tuple) * 0.10) if config.eval_set else 0

            train_x.extend(zip(five_tuple[:train_size], seq[:train_size]))  # 同时保存 five 和 seq
            train_y.extend([label] * train_size)
            valid_x.extend(zip(five_tuple[train_size:train_size + valid_size], seq[train_size:train_size + valid_size]))
            valid_y.extend([label] * valid_size)
            test_x.extend(zip(five_tuple[train_size + valid_size:], seq[train_size + valid_size:]))
            test_y.extend([label] * (len(five_tuple) - train_size - valid_size))
        # train_x, train_y, valid_x, valid_y, test_x, test_y = map(np.array, [train_x, train_y, valid_x, valid_y, test_x, test_y])
        max_value = 1
        return train_x, train_y, valid_x, valid_y, test_x, test_y, max_value


class TensorDataset(torch.utils.data.Dataset):
    def __init__(self, all_x, all_y, config):
        self.config = config
        self.all_x = all_x
        self.all_y = all_y

    def __len__(self):
        return len(self.all_x)

    def __getitem__(self, idx):
        context_info, seq_input = self.all_x[idx]
        context_info = torch.as_tensor(context_info, dtype=torch.float32)
        timestamp = torch.as_tensor(seq_input)[:, 0]
        seq_input = torch.as_tensor(seq_input)[:,-1]
        # 0 Padding，注意这里是否有误
        padded_seq = torch.zeros(self.config.max_length, dtype=seq_input.dtype)
        padded_seq[:seq_input.size(0)] = seq_input
        seq_input = padded_seq
        labels = self.all_y[idx]
        return context_info, seq_input, labels


def custom_collate_fn(batch, config):
    from torch.utils.data.dataloader import default_collate
    inputs, seq_input, labels = zip(*batch)
    context_info = default_collate(inputs)
    seq_input = default_collate(seq_input)
    labels = torch.as_tensor(labels, dtype=torch.long if config.classification else torch.float32)
    return context_info, seq_input, labels


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
