# coding : utf-8
# Author : Yuxiang Zeng
import torch
from dask.cli import config_get

from modules.predictor import Predictor
import pickle

class Backbone(torch.nn.Module):
    def __init__(self, config):
        super(Backbone, self).__init__()
        self.config = config
        self.rank = config.rank
        # First Step
        # self.transfer = torch.nn.Linear(5, self.rank)
        # self.lstm = torch.nn.LSTM(self.rank, self.rank, num_layers=1, bias=True, batch_first=False, dropout=0, bidirectional=False)

        with open(f'./datasets/flow/{config.dataset}_info.pickle', 'rb') as f:
            info = pickle.load(f)
            max_flow_length = info['max_flow_length']
            num_classes = info['num_classes']
        self.lstm = torch.nn.Linear(max_flow_length, self.rank)

        self.predictor = Predictor(
            input_dim=config.rank,
            hidden_dim=config.rank,
            output_dim=num_classes,
            n_layer=3,
            init_method='xavier'
        )

    def forward(self, time_stamp, seq_input):
        # context_embeds = self.transfer(time_stamp)
        # print(seq_input.shape)
        seq_embeds = self.lstm(seq_input)
        # final_inputs = torch.cat([context_embeds, seq_embeds], dim = -1)
        y = self.predictor(seq_embeds)
        return y
