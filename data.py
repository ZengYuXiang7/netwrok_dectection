# coding : utf-8
# Author : yuxiang Zeng

import numpy as np
import torch

from utils.config import get_config
from utils.logger import Logger
from utils.plotter import MetricsPlotter
from utils.utils import set_settings
from scipy.sparse import csr_matrix
from PIL import Image
import os
from torchvision.transforms import Compose, ToTensor, Normalize, Resize, InterpolationMode
from torchvision.transforms import Compose, Resize, CenterCrop, RandomHorizontalFlip, RandomResizedCrop, ToTensor, Normalize, InterpolationMode

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
        self.train_image_tensor, self.train_y_tensor, self.valid_image_tensor, self.valid_y_tensor, self.test_image_tensor, self.test_y_tensor, self.max_value = self.get_train_valid_test_dataset(
            self.x, self.y, config) if not config.classification else self.get_train_valid_test_classification_dataset(self.x, self.y, config)
        self.train_set, self.valid_set, self.test_set = self.get_dataset(self.train_image_tensor, self.train_y_tensor, self.valid_image_tensor, self.valid_y_tensor, self.test_image_tensor, self.test_y_tensor, config)
        self.train_loader, self.valid_loader, self.test_loader = get_dataloaders(self.train_set, self.valid_set, self.test_set, config)
        config.log.only_print(f'Train_length : {len(self.train_loader.dataset)} Valid_length : {len(self.valid_loader.dataset)} Test_length : {len(self.test_loader.dataset)} Max_value : {self.max_value:.2f}')

    def get_dataset(self, train_image_tensor, train_y_tensor, valid_image_tensor, valid_y_tensor, test_image_tensor, test_y_tensor, config):
        return (
            TensorDataset(train_image_tensor, train_y_tensor, config),
            TensorDataset(valid_image_tensor, valid_y_tensor, config),
            TensorDataset(test_image_tensor, test_y_tensor, config)
        )

    def get_train_valid_test_dataset(self, image_tensor, y, config):
        image_tensor, y = np.array(image_tensor), np.array(y)
        indices = np.random.permutation(len(image_tensor))
        image_tensor, y = image_tensor[indices], y[indices]

        if not config.classification:
            max_value = y.max()
            y /= max_value
        else:
            max_value = 1

        train_size = int(len(image_tensor) * config.density)
        if config.eval_set:
            valid_size = int(len(image_tensor) * 0.10)
        else:
            valid_size = 0

        train_image_tensor = image_tensor[:train_size]
        train_y_tensor = y[:train_size]

        valid_image_tensor = image_tensor[train_size:train_size + valid_size]
        valid_y_tensor = y[train_size:train_size + valid_size]

        test_image_tensor = image_tensor[train_size + valid_size:]
        test_y_tensor = y[train_size + valid_size:]

        return train_image_tensor, train_y_tensor, valid_image_tensor, valid_y_tensor, test_image_tensor, test_y_tensor, max_value

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
        train_image_tensor = np.array(train_images)
        train_y_tensor = np.array(train_labels)
        valid_image_tensor = np.array(valid_images)
        valid_y_tensor = np.array(valid_labels)
        test_image_tensor = np.array(test_images)
        test_y_tensor = np.array(test_labels)
        max_value = 1
        return train_image_tensor, train_y_tensor, valid_image_tensor, valid_y_tensor, test_image_tensor, test_y_tensor, max_value


def _convert_to_rgb(image):
    return image.convert('RGB')

class TensorDataset(torch.utils.data.Dataset):
    def __init__(self, all_image_address, all_y, config):
        self.config = config
        self.all_image_address = all_image_address
        self.all_y = all_y
        self.preprocess = self.get_preprocess()

    def get_preprocess(self):
        transform = Compose([
            Resize(256, interpolation=InterpolationMode.BICUBIC),  # Resize to _RESIZE_SIDE_MIN
            CenterCrop((224, 224)),  # Center crop to HEIGHT and WIDTH
            RandomHorizontalFlip(),  # Apply random horizontal flip
            RandomResizedCrop((224, 224), scale=(0.5, 1.0), ratio=(1.0, 1.0)),  # Random crop and resize
            ToTensor(),  # Convert to tensor
            Normalize(mean=[123.68 / 255, 116.78 / 255, 103.94 / 255], std=[1.0 / 255, 1.0 / 255, 1.0 / 255])
            # Normalize with _R_MEAN, _G_MEAN, _B_MEAN and _R_STD, _G_STD, _B_STD
        ])
        # transform = Compose([
        #     Resize((224, 224), interpolation=InterpolationMode.BICUBIC),
        #     _convert_to_rgb,
        #     ToTensor(),
        #     Normalize((0.48145466, 0.4578275, 0.40821073), (0.26862954, 0.26130258, 0.27577711)),
        # ])
        return transform

    def __len__(self):
        return len(self.all_image_address)

    def __getitem__(self, idx):
        file_name = self.all_image_address[idx]
        raw_image = Image.open(file_name)
        image_tensor = self.preprocess(raw_image)
        label = self.all_y[idx]
        return image_tensor, label

def custom_collate_fn(batch, config):
    from torch.utils.data.dataloader import default_collate
    image_tensor, label = zip(*batch)
    image_tensor = default_collate(image_tensor)
    label = torch.as_tensor(label, dtype=torch.long)
    return image_tensor, label


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
