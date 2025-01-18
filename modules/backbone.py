# coding : utf-8
# Author : Yuxiang Zeng
from typing import final

import torch

from modules.attention import ExternalAttention
from modules.dft import DFT
from modules.predictor import Predictor
import pickle

from modules.seq_encoder import SeqEncoder


class Backbone(torch.nn.Module):
    def __init__(self, config):
        super(Backbone, self).__init__()
        self.config = config
        self.rank = config.rank

        # First Step
        with open(f'./datasets/flow/{config.dataset}_info_{config.flow_length_limit}.pickle', 'rb') as f:
            info = pickle.load(f)
            num_classes = info['num_classes']

        # TimeStamp encoder
        self.time_transfer = torch.nn.Sequential(
            torch.nn.Linear(config.flow_length_limit, self.rank),
        )

        # Flow encoder
        if config.try_exp == 1:
            self.scales = [15, 10, 6, 5, 3, 1]  # 常规递减分布
        elif config.try_exp == 3:
            self.scales = [10, 6, 5, 3, 2, 1]  # 偏向小尺度的分布
        elif config.try_exp == 5:
            self.scales = [15, 10, 5, 3, 1]  # 更稀疏的分布
        elif config.try_exp == 7:
            self.scales = [15, 10, 6, 5, 1]  # 排除较小的2和3
        elif config.try_exp == 8:
            self.scales = [15, 10, 6, 3, 1]  # 适中范围的小尺度分布
        elif config.try_exp == 9:
            self.scales = [10, 6, 3, 2, 1]  # 最偏向小尺度的分布
        elif config.try_exp == 10:
            self.scales = [15, 10, 6, 5, 3, 2, 1]  # 最全面的分布

        self.scales = [10, 6, 3, 2, 1]  # 最偏向小尺度的分布

        self.patch_encoder = torch.nn.Sequential(
            *[SeqEncoder(1, config.rank, config.flow_length_limit // self.scales[i], config.num_layers, config) for i in range(len(self.scales))]
        )

        self.fusion_layer = torch.nn.ModuleList()
        for i in range(len(self.scales)):
            self.fusion_layer.append(
                torch.nn.Sequential(
                    torch.nn.Linear(config.rank * 2, config.rank),
                    torch.nn.ReLU(),
                    torch.nn.Linear(config.rank, config.rank)
                )
            )

        final_input_dim = config.rank * 1
        self.predictor = Predictor(
            input_dim=final_input_dim,
            hidden_dim=config.rank,
            output_dim=num_classes,
            n_layer=3,
            init_method='xavier'
        )

    # def forward(self, time_interval, x):
    #     # 编码时间间隔与流序列
    #     # time_embeds = self.time_transfer(time_interval)
    #     x = torch.abs(x)
    #     patch_embedding = []
    #     for i in range(len(self.scales)):
    #         now_x = x[:, ::self.scales[i]]
    #         patch_embedding.append(self.patch_encoder[i](now_x))
    #     x = torch.stack(patch_embedding, dim=1)
    #     x = torch.mean(x, dim=1)
    #     y = self.predictor(x)
    #     return y


    def forward(self, time_interval, x):
        x = torch.abs(x)
        h_out = None
        for i in range(len(self.scales)):
            now_x = x[:, ::self.scales[i]]
            now_patch_embedding = self.patch_encoder[i](now_x)
            if i == 0:
                h_out = now_patch_embedding
            else:
                now_patch_embedding = torch.cat((now_patch_embedding, h_out), dim=-1)
                h_out = self.fusion_layer[i](now_patch_embedding)
        x = h_out
        y = self.predictor(x)
        return y


