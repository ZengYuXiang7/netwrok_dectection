# coding : utf-8
# Author : Yuxiang Zeng


import torch
import torch.nn as nn
import pickle

class MLP(torch.nn.Module):
    def __init__(self, config):
        super(MLP, self).__init__()

        with open(f'./datasets/flow/{config.dataset}_info_{config.flow_length_limit}.pickle', 'rb') as f:
            info = pickle.load(f)
            max_flow_length = info['max_flow_length']
            num_classes = info['num_classes']
        self.config = config
        input_size = max_flow_length
        hidden_size = config.rank

        # 定义三层网络
        self.fc1 = nn.Linear(input_size, hidden_size)  # 第一层全连接
        self.ln1 = nn.LayerNorm(hidden_size)  # 第一层 LayerNorm
        self.act1 = nn.ReLU()  # 第一层激活函数

        self.fc2 = nn.Linear(hidden_size, hidden_size)  # 第二层全连接
        self.ln2 = nn.LayerNorm(hidden_size)  # 第二层 LayerNorm
        self.act2 = nn.ReLU()  # 第二层激活函数

        self.fc3 = nn.Linear(hidden_size, num_classes)  # 第三层全连接
        self.ln3 = nn.LayerNorm(num_classes)  # 第三层 LayerNorm
        self.act3 = nn.ReLU()  # 第三层激活函数

        if config.stat:
            self.feature_tf = torch.nn.Linear(39, config.rank)
            self.fc = nn.Linear(hidden_size * 2, num_classes)  # 全连接层

    def forward(self, flow_feature, x):
        # 前向传播
        x = torch.abs(x)
        x = self.fc1(x)
        x = self.ln1(x)
        x = self.act1(x)

        x = self.fc2(x)
        x = self.ln2(x)
        x = self.act2(x)

        # 全连接层
        if self.config.stat:
            feature_embeds = self.feature_tf(flow_feature)
            final_input = torch.cat((x, feature_embeds), 1)
            y = self.fc(final_input)
        else:
            x = self.fc3(x)
            x = self.ln3(x)
            y = self.act3(x)
        return y