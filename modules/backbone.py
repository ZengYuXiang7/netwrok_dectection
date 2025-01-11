# coding : utf-8
# Author : Yuxiang Zeng
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
        self.time_transfer = torch.nn.Linear(max_flow_length, self.rank)

        # Position Encoding
        self.pos_embedding = torch.nn.Parameter(torch.randn(1, max_flow_length, self.rank))
        self.pos_norm = torch.nn.LayerNorm(self.rank)

        # Flow encoder
        self.seq_transfer = torch.nn.Linear(1, self.rank)
        self.seq_encoder = SeqEncoder(config)

        self.dropout = torch.nn.Dropout(0.1)
        self.MLP1 = torch.nn.Sequential(
            torch.nn.Linear(self.rank, self.rank),
            torch.nn.GELU(),
            torch.nn.Linear(self.rank, self.rank)
        )
        self.seq_output_norm1 = torch.nn.LayerNorm(self.rank)
        self.seq_output_norm2 = torch.nn.LayerNorm(self.rank)
        self.seq_output_transfer = torch.nn.Linear(max_flow_length * self.rank, self.rank)

        # FFT
        self.fft_calculator = DFT(config)
        self.fft_transfer = torch.nn.Linear(max_flow_length, self.rank)

        # Merge info
        # self.merge_info = torch.nn.Linear(max_flow_length * 2, self.rank)

        self.predictor = Predictor(
            input_dim=config.rank * 3,
            hidden_dim=config.rank,
            output_dim=num_classes,
            n_layer=4,
            init_method='xavier'
        )

    def forward(self, time_interval, seq_input, merge_info):
        # 编码时间间隔与流序列
        time_embeds = self.time_transfer(time_interval)

        # FFT
        seq_input = torch.abs(seq_input)
        seq_season, seq_trend = self.fft_calculator.forward(seq_input)
        seq_season = self.fft_transfer(seq_season)

        # 位置编码
        # batch_size, seq_len, _ = lstm_input.shape
        # pos_embed = self.pos_embedding
        # lstm_input = lstm_input + pos_embed
        # lstm_input = self.pos_norm(lstm_input)

        # 序列学习,  编码流序列
        seq_input = seq_input.unsqueeze(-1)
        seq_embeds = self.seq_transfer(seq_input)
        seq_enc = self.seq_encoder(seq_embeds)

        seq_embeds = seq_embeds + self.dropout(seq_enc)
        seq_embeds = self.seq_output_norm1(seq_embeds)
        seq_embeds = seq_embeds + self.dropout(self.MLP1(seq_embeds))
        seq_embeds = self.seq_output_norm2(seq_embeds)

        # Flatten
        seq_embeds = seq_embeds.reshape(seq_embeds.shape[0], -1)
        seq_embeds = self.seq_output_transfer(seq_embeds)

        # Merge Information
        # merge_embeds = self.merge_info(merge_info)

        a = self.pos(time_embeds, seq_embeds, seq_embeds)

        final_inputs = torch.cat([time_embeds, seq_season, seq_embeds], dim=-1)
        # 特征融合
        y = self.predictor(final_inputs)
        return y



