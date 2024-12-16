# coding : utf-8
# Author : Yuxiang Zeng
import torch
from dask.cli import config_get

from modules.predictor import Predictor


class Backbone(torch.nn.Module):
    def __init__(self, config):
        super(Backbone, self).__init__()
        self.config = config
        self.rank = config.rank
        # First Step
        self.transfer = torch.nn.Linear(5, self.rank)
        # self.lstm = torch.nn.LSTM(self.rank, self.rank, num_layers=1, bias=True, batch_first=False, dropout=0, bidirectional=False)
        self.lstm = torch.nn.Linear(self.config.max_length, self.rank)

        self.predictor = Predictor(
            input_dim=config.rank * 2,
            hidden_dim=config.rank,
            output_dim=config.num_classes,
            n_layer=3,
            init_method='xavier'
        )

    def forward(self, context_info, seq_input):
        context_embeds = self.transfer(context_info)
        # print(seq_input.shape)
        seq_embeds = self.lstm(seq_input)
        final_inputs = torch.cat([context_embeds, seq_embeds], dim = -1)
        y = self.predictor(final_inputs)
        return y
