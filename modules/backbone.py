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
            max_flow_length = info['max_flow_length']
            num_classes = info['num_classes']

        # TimeStamp encoder
        self.time_transfer = torch.nn.Sequential(
            torch.nn.Linear(max_flow_length, self.rank),
        )

        # Flow encoder
        self.seq_encoder1 = SeqEncoder(1, config)
        self.seq_encoder2 = SeqEncoder(1, config)

        final_input_dim = config.rank * 1
        self.predictor = Predictor(
            input_dim=final_input_dim,
            hidden_dim=config.rank,
            output_dim=num_classes,
            n_layer=3,
            init_method='xavier'
        )


    def forward(self, time_interval, x, merge_info):
        # 编码时间间隔与流序列
        time_embeds = self.time_transfer(time_interval)

        # 创建掩码
        mask_positive = x > 0  # 正值掩码
        mask_negative = x < 0  # 负值掩码
        # 提取正值和负值，并保持形状
        x1 = x.clone()
        x1[~mask_positive] = 0  # 将非正值置为 0
        x2 = x.clone()
        x2[~mask_negative] = 0  # 将非负值置为 0
        x2 = abs(x2)  # 将负值取绝对值

        # 通过 single_direction 处理
        x1 = self.seq_encoder1(x1)
        x2 = self.seq_encoder2(x2)
        x = x1 + x2

        # seq_remain = seq_embeds - seq_season
        # final_inputs = torch.stack([seq_remain, seq_embeds], dim=1)
        # att_inputs = final_inputs
        # att_outputs, _ = self.att_fusion(final_inputs, final_inputs, final_inputs)
        # final_inputs = att_inputs + att_outputs
        # final_inputs = final_inputs.reshape(final_inputs.shape[0], -1)
        # final_inputs = 0.9 * x + 0.1 * time_embeds
        final_inputs = x

        # 特征融合
        y = self.predictor(final_inputs)

        return y
