# coding : utf-8
# Author : Yuxiang Zeng
import torch
from dask.cli import config_get

from modules.predictor import Predictor


class Backbone(torch.nn.Module):
    def __init__(self, config):
        super(Backbone, self).__init__()
        self.config = config
        # First Step
        self.transfer = torch.nn.Linear(5, config.rank)
        self.lstm = torch.nn.LSTM()

        self.predictor = Predictor(
            input_dim=config.rank,
            hidden_dim=config.rank,
            output_dim=config.num_classes,
            n_layer=3,
            init_method='xavier'
        )

    def forward(self, context_info, seq_input):
        context_embeds = self.transfer(context_info)
        seq_embeds = self.lstm(seq_input)
        final_inputs = torch.cat([context_embeds, seq_embeds], dim = -1)
        y = self.predictor(final_inputs)
        return y
