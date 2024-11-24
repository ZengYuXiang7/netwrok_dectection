# coding : utf-8
# Author : Yuxiang Zeng
import torch

from modules.predictor import Predictor


class Backbone(torch.nn.Module):
    def __init__(self, config):
        super(Backbone, self).__init__()
        self.config = config
        # First Step

        self.predictor = Predictor(
            input_dim=config.rank,
            hidden_dim=config.rank,
            output_dim=config.num_classes,
            n_layer=3,
            init_method='xavier'
        )

    def forward(self, x):
        y = self.predictor(x)
        return y
