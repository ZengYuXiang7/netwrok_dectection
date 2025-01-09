# coding : utf-8
# Author : Yuxiang Zeng

import torch
import torch.nn as nn
import pickle

class LSTMModel(torch.nn.Module):
    def __init__(self, config):
        super(LSTMModel, self).__init__()

        # 从配置文件加载信息
        with open(f'./datasets/flow/{config.dataset}_info_{config.flow_length_limit}.pickle', 'rb') as f:
            info = pickle.load(f)
            max_flow_length = info['max_flow_length']  # 输入流的最大长度
            num_classes = info['num_classes']  # 分类的类别数

        hidden_size = config.rank  # 隐藏层大小
        input_size = max_flow_length

        # 定义 LSTM 网络
        self.lstm = nn.LSTM(input_size=1,
                            hidden_size=hidden_size,
                            num_layers=2,  # 双层 LSTM
                            batch_first=True,  # 输入的 batch 在第一个维度
                            dropout=0.3,  # 使用 Dropout 正则化
                            bidirectional=False)  # 单向 LSTM

        # 全连接层，用于分类
        self.fc = nn.Linear(hidden_size * max_flow_length, num_classes)  # 输出分类结果

    def forward(self, _, x):
        # x: [batch_size, max_flow_length]
        x = x.unsqueeze(-1)
        # print(x.shape)
        # exit()
        out, (hn, cn) = self.lstm(x)  # out: [batch_size, max_flow_length, hidden_size]
        out = out.reshape(out.shape[0], -1)
        y = self.fc(out)  # 输出分类结果，形状为 [batch_size, num_classes]
        # print(y.shape)
        return y
