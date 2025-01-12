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

        self.dropout = torch.nn.Dropout(0.1)

        # TimeStamp encoder
        self.time_transfer = torch.nn.Sequential(
            torch.nn.Linear(max_flow_length, self.rank),
            torch.nn.LayerNorm(self.rank),
        )

        # Position Encoding
        self.pos_embedding = torch.nn.Parameter(torch.randn(1, max_flow_length, self.rank))
        self.pos_norm = torch.nn.LayerNorm(self.rank)

        # Flow encoder
        self.seq_transfer = torch.nn.Linear(1, self.rank)
        self.seq_encoder = torch.nn.ModuleList(
            [SeqEncoder(config) for _ in range(config.num_layers)]
        )

        self.seq_output_transfer = torch.nn.Linear(max_flow_length * self.rank, self.rank)

        # FFT
        self.fft_calculator = DFT(config)
        self.fft_transfer = torch.nn.Linear(max_flow_length, self.rank)

        # Merge info
        # self.merge_info = torch.nn.Linear(max_flow_length * 2, self.rank)

        if self.config.try_exp in [1, 2, 3, 4, 10, 11, 12, 19]:
            final_input_dim = config.rank * 1
        elif self.config.try_exp in [5, 6, 17, 18]:
            final_input_dim = config.rank * 3
        elif self.config.try_exp in [7, 8, 9, 14, 15, 16, 20]:
            final_input_dim = config.rank * 2
        elif self.config.try_exp in [13]:
            final_input_dim = config.rank * 4

        self.predictor = Predictor(
            input_dim=final_input_dim,
            hidden_dim=config.rank,
            output_dim=num_classes,
            n_layer=3,
            init_method='xavier'
        )

        if self.config.try_exp >= 11:
            self.att_fusion = torch.nn.MultiheadAttention(self.rank, num_heads=2, dropout=0.1, batch_first=True)

    def forward(self, time_interval, seq_input, merge_info):
        # 编码时间间隔与流序列
        time_embeds = self.time_transfer(time_interval)

        # 位置编码
        # batch_size, seq_len, _ = lstm_input.shape
        # pos_embed = self.pos_embedding
        # lstm_input = lstm_input + pos_embed
        # lstm_input = self.pos_norm(lstm_input)

        # FFT
        seq_input = torch.abs(seq_input)
        seq_season, seq_trend = self.fft_calculator.forward(seq_input)
        seq_season = self.fft_transfer(seq_season)

        # 序列学习,  编码流序列
        seq_input = seq_input.unsqueeze(-1)
        seq_embeds = self.seq_transfer(seq_input)

        for i in range(self.config.num_layers):
            seq_embeds = seq_embeds + self.seq_encoder[i](seq_embeds)

        # Flatten
        seq_embeds = seq_embeds.reshape(seq_embeds.shape[0], -1)
        seq_embeds = self.seq_output_transfer(seq_embeds)

        seq_remain = seq_embeds - seq_season

        # Fusion
        if self.config.try_exp == 1:
            final_inputs = seq_remain + seq_embeds
        elif self.config.try_exp == 2:
            final_inputs = seq_season + seq_embeds
        elif self.config.try_exp == 3:
            final_inputs = time_embeds + seq_embeds + seq_season
        elif self.config.try_exp == 4:
            final_inputs = time_embeds + seq_embeds + seq_remain
        elif self.config.try_exp == 5:
            final_inputs = torch.cat([time_embeds, seq_season, seq_embeds], dim=-1)
        elif self.config.try_exp == 6:
            final_inputs = torch.cat([time_embeds, seq_remain, seq_embeds], dim=-1)
        elif self.config.try_exp == 7:
            final_inputs = torch.cat([seq_remain, seq_embeds], dim=-1)
        elif self.config.try_exp == 8:
            final_inputs = torch.cat([time_embeds, seq_embeds], dim=-1)
        elif self.config.try_exp == 9:
            final_inputs = torch.cat([seq_season, seq_embeds], dim=-1)
        elif self.config.try_exp == 10:
            final_inputs = seq_embeds
        elif self.config.try_exp == 11:
            final_inputs = torch.stack([time_embeds, seq_remain, seq_season, seq_embeds], dim=1)
            final_inputs, _ = self.att_fusion(final_inputs, final_inputs, final_inputs)
            final_inputs = torch.sum(final_inputs, dim=1)
        elif self.config.try_exp == 12:
            final_inputs = torch.stack([time_embeds, seq_remain, seq_season, seq_embeds], dim=1)
            final_inputs, _ = self.att_fusion(final_inputs, final_inputs, final_inputs)
            final_inputs = torch.mean(final_inputs, dim=1)
        elif self.config.try_exp == 13:
            final_inputs = torch.stack([time_embeds, seq_remain, seq_season, seq_embeds], dim=1)
            final_inputs, _ = self.att_fusion(final_inputs, final_inputs, final_inputs)
            final_inputs = final_inputs.reshape(final_inputs.shape[0], -1)
        elif self.config.try_exp == 14:
            final_inputs = torch.stack([time_embeds, seq_embeds], dim=1)
            final_inputs, _ = self.att_fusion(final_inputs, final_inputs, final_inputs)
            final_inputs = final_inputs.reshape(final_inputs.shape[0], -1)
        elif self.config.try_exp == 15:
            final_inputs = torch.stack([seq_season, seq_embeds], dim=1)
            final_inputs, _ = self.att_fusion(final_inputs, final_inputs, final_inputs)
            final_inputs = final_inputs.reshape(final_inputs.shape[0], -1)
        elif self.config.try_exp == 16:
            final_inputs = torch.stack([seq_remain, seq_embeds], dim=1)
            final_inputs, _ = self.att_fusion(final_inputs, final_inputs, final_inputs)
            final_inputs = final_inputs.reshape(final_inputs.shape[0], -1)
        elif self.config.try_exp == 17:
            final_inputs = torch.stack([time_embeds, seq_season, seq_embeds], dim=1)
            final_inputs, _ = self.att_fusion(final_inputs, final_inputs, final_inputs)
            final_inputs = final_inputs.reshape(final_inputs.shape[0], -1)
        elif self.config.try_exp == 18:
            final_inputs = torch.stack([time_embeds, seq_remain, seq_embeds], dim=1)
            final_inputs, _ = self.att_fusion(final_inputs, final_inputs, final_inputs)
            final_inputs = final_inputs.reshape(final_inputs.shape[0], -1)
        elif self.config.try_exp == 19:
            time_embeds = time_embeds.unsqueeze(1)
            seq_embeds = seq_season.unsqueeze(1)
            final_inputs, _ = self.att_fusion(time_embeds, seq_embeds, seq_embeds)
            final_inputs = final_inputs.squeeze(1)
        elif self.config.try_exp == 20:
            time_embeds = time_embeds.unsqueeze(1)
            seq_embeds = seq_season.unsqueeze(1)
            final_inputs1, _ = self.att_fusion(time_embeds, seq_embeds, seq_embeds)
            final_inputs2, _ = self.att_fusion(time_embeds, seq_embeds, seq_embeds)
            final_inputs1 = final_inputs1.squeeze(1)
            final_inputs2 = final_inputs2.squeeze(1)
            final_inputs = torch.cat([final_inputs1, final_inputs2], dim=1)

        # 特征融合
        y = self.predictor(final_inputs)
        return y



