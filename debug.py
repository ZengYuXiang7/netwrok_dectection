# coding : utf-8
# Author : Yuxiang Zeng
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import os
from tqdm import *

def draw_one_plot(i, seq, label, save_dir='./figs'):
    """
    绘制并保存给定序列的图像。

    参数：
    - i (int): 序列的索引。
    - seq (array_like): 要绘制的序列数据。
    - save_dir (str, optional): 保存图像的目录。默认为'./figs'。
    """
    # 确保保存目录存在
    os.makedirs(save_dir, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(seq, label=f'Sequence {i}', color='blue')  # 绘制序列
    plt.axhline(y=0, color='red', linestyle='--', label='y=0')  # 在y=0处绘制水平线
    plt.title(f'Sequence {i} Flow ----- flow-length={len(seq)} ---- label = {label}')
    plt.xlabel('Time Steps')
    plt.ylabel('Flow Value')
    plt.legend()
    plt.grid(True)

    # 构造文件路径
    file_path = os.path.join(save_dir, f'{i}_flow.png')

    # 保存图像到指定路径
    plt.savefig(file_path)
    plt.close()  # 关闭图像以释放内存


if __name__ == '__main__':
    # Experiment Settings, logger, plotter
    from utils.config import get_config
    config = get_config()
    from utils.logger import Logger
    from utils.plotter import MetricsPlotter
    from utils.utils import set_settings, set_seed
    set_settings(config)
    log_filename = f'Model_{config.model}_Dataset_{config.dataset}_W{config.time_interval:d}_R{config.rank}'
    plotter = MetricsPlotter(log_filename, config)
    log = Logger(log_filename, plotter, config)
    # Set seed of this round
    set_seed(config.seed + 0)
    # Initialize the data and the model
    from data import experiment, DataModule
    exper = experiment(config)
    datamodule = DataModule(exper, config)

    dataset_info = pickle.load(open(f'./datasets/flow/{config.dataset}_info_{config.flow_length_limit}.pickle', 'rb'))
    max_packet_length = dataset_info['max_packet_length']
    max_flow_length = dataset_info['max_flow_length']

    import random
    total_sequences = len(datamodule.train_set.x)
    indices = list(range(total_sequences))
    random.shuffle(indices)
    # for idx in trange(total_sequences, desc="Saving plots"):
    #     i = indices[idx]  # Get the shuffled index
    #     seq_input = datamodule.train_set.x[i]
    #     seq = seq_input[config.flow_length_limit:]
    #     label = datamodule.train_set.y[i]
    #     draw_one_plot(i, seq, label)

    def f(idx):
        i = indices[idx]  # Get the shuffled index
        seq_input = datamodule.train_set.x[i]
        seq = seq_input[config.flow_length_limit:]
        label = datamodule.train_set.y[i]
        draw_one_plot(i, seq, label)


    import multiprocessing
    with multiprocessing.Pool(processes=16) as pool:
        for _ in tqdm(pool.imap(f, indices), total=len(indices)):
            pass
