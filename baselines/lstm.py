# coding : utf-8
# Author : Yuxiang Zeng

import torch
import torch.nn as nn
import pickle

class LSTMModel(torch.nn.Module):
    def __init__(self, config):
        super(LSTMModel, self).__init__()

        # 从配置文件加载信息
        with open(f'./datasets/flow/{config.dataset}_info.pickle', 'rb') as f:
            info = pickle.load(f)
            max_flow_length = info['max_flow_length']  # 输入流的最大长度
            num_classes = info['num_classes']  # 分类的类别数

        hidden_size = config.rank  # 隐藏层大小
        input_size = 1  # 每个数据点的特征数（此处只有 packet length）

        # 定义 LSTM 网络
        self.lstm = nn.LSTM(input_size=input_size,
                            hidden_size=hidden_size,
                            num_layers=2,  # 双层 LSTM
                            batch_first=True,  # 输入的 batch 在第一个维度
                            dropout=0.3,  # 使用 Dropout 正则化
                            bidirectional=False)  # 单向 LSTM

        # 全连接层，用于分类
        self.fc = nn.Linear(hidden_size, num_classes)  # 输出分类结果

    def forward(self, _, x):
        # x: [batch_size, max_flow_length]
        x = x.unsqueeze(-1)  # 扩展最后一个维度，形状变为 [batch_size, max_flow_length, 1]

        # LSTM 网络
        out, (hn, cn) = self.lstm(x)  # out: [batch_size, max_flow_length, hidden_size]
        last_output = out[:, -1, :]  # 取 LSTM 最后一时刻的输出，形状 [batch_size, hidden_size]

        # 全连接层
        y = self.fc(last_output)  # 输出分类结果，形状为 [batch_size, num_classes]
        return y

# 示例用法
if __name__ == "__main__":
    class Config:
        dataset = "example_dataset"
        rank = 64

    config = Config()

    model = LSTMModel(config)
    print(model)

    # 输入一个随机张量进行测试
    batch_size = 16
    max_flow_length = 128  # 假设配置中的最大流长度
    x = torch.rand((batch_size, max_flow_length))  # 输入形状 [batch_size, max_flow_length]

    output = model(None, x)  # 调用前向传播
    print("Output shape:", output.shape)