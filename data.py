# coding : utf-8
# Author : yuxiang Zeng

import torch
import numpy as np
from utils.config import get_config
from utils.logger import Logger
from utils.plotter import MetricsPlotter
from utils.utils import set_settings

class experiment:
    def __init__(self, config):
        self.config = config

    @staticmethod
    def load_data(config):
        import os
        from sklearn.preprocessing import LabelEncoder

        # Set the path to the root folder of the dataset
        root_dir = 'datasets/foods'

        # Lists to store image paths and corresponding labels
        x = []
        label = []

        # Iterate over each folder in the dataset directory
        for lbl in os.listdir(root_dir):
            label_dir = os.path.join(root_dir, lbl)

            # Check if it's a directory (to ignore files like foods.zip)
            if os.path.isdir(label_dir):
                # Iterate over each image in the label directory
                for image_name in os.listdir(label_dir):
                    image_path = os.path.join(label_dir, image_name)

                    # Append the image path and label to their respective lists
                    x.append(image_path)
                    label.append(lbl)

        # Perform label encoding on the labels
        label_encoder = LabelEncoder()
        y = label_encoder.fit_transform(label)

        return x, y

    @staticmethod
    def preprocess_data(data, config):
        return data

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

    def get_train_valid_test_dataset(self, x, y, config):
        x, y = np.array(x), np.array(y)
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
        x, y = np.array(x), np.array(y)
        from collections import defaultdict
        class_data = defaultdict(list)
        for img, label in zip(x, y):
            class_data[label].append(img)
        train_images, train_labels = [], []
        valid_images, valid_labels = [], []
        test_images, test_labels = [], []
        for label, images in class_data.items():
            images = np.array(images)
            np.random.shuffle(images)
            train_size = int(len(images) * config.density)
            valid_size = int(len(images) * 0.10) if config.eval_set else 0
            train_images.extend(images[:train_size])
            train_labels.extend([label] * train_size)
            valid_images.extend(images[train_size:train_size + valid_size])
            valid_labels.extend([label] * valid_size)
            test_images.extend(images[train_size + valid_size:])
            test_labels.extend([label] * (len(images) - train_size - valid_size))
        train_x = np.array(train_images)
        train_y = np.array(train_labels)
        valid_x = np.array(valid_images)
        valid_y = np.array(valid_labels)
        test_x = np.array(test_images)
        test_y = np.array(test_labels)
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
        inputs = self.all_x[idx]
        values = self.all_y[idx]
        return inputs, values


def custom_collate_fn(batch, config):
    from torch.utils.data.dataloader import default_collate
    inputs, values = zip(*batch)
    inputs = torch.as_tensor(inputs, dtype=torch.float32)
    values = torch.as_tensor(values, dtype=torch.long)
    return inputs, values


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
