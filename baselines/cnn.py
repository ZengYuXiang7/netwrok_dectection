# coding : utf-8
# Author : Yuxiang Zeng

import torch
import torch.nn as nn
import pickle

class CNN(torch.nn.Module):
    def __init__(self, config):
        super(CNN, self).__init__()

        # 从配置文件加载信息
        with open(f'./datasets/flow/{config.dataset}_info_{config.flow_length_limit}.pickle', 'rb') as f:
            info = pickle.load(f)
            max_flow_length = info['max_flow_length']  # 输入流的最大长度
            num_classes = info['num_classes']  # 分类的类别数

        input_size = max_flow_length
        hidden_size = config.rank

        # 定义 CNN 网络
        self.conv1 = nn.Conv1d(in_channels=1, out_channels=hidden_size, kernel_size=3, padding=1)  # 第一层卷积
        self.ln1 = nn.LayerNorm(hidden_size)  # 第一层 LayerNorm
        self.act1 = nn.ReLU()  # 第一层激活函数

        self.conv2 = nn.Conv1d(in_channels=hidden_size, out_channels=hidden_size, kernel_size=3, padding=1)  # 第二层卷积
        self.ln2 = nn.LayerNorm(hidden_size)  # 第二层 LayerNorm
        self.act2 = nn.ReLU()  # 第二层激活函数

        self.pool = nn.AdaptiveAvgPool1d(1)  # 自适应全局平均池化，降维
        self.fc = nn.Linear(hidden_size, num_classes)  # 全连接层

    def forward(self, _, x, __):
        # x: [batch_size, max_flow_length]
        x = x.unsqueeze(1)  # 扩展通道维度，形状变为 [batch_size, 1, max_flow_length]

        # 第一层卷积
        x = self.conv1(x)  # 卷积层
        x = self.ln1(x.transpose(1, 2)).transpose(1, 2)  # LayerNorm 操作
        x = self.act1(x)  # 激活函数

        # 第二层卷积
        x = self.conv2(x)  # 卷积层
        x = self.ln2(x.transpose(1, 2)).transpose(1, 2)  # LayerNorm 操作
        x = self.act2(x)  # 激活函数

        # 池化降维
        x = self.pool(x).squeeze(-1)  # 形状变为 [batch_size, hidden_size]

        # 全连接层
        y = self.fc(x)  # 输出分类结果，形状为 [batch_size, num_classes]
        return y