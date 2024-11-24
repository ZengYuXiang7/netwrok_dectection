# coding : utf-8
# Author : yuxiang Zeng
import torch


class Predictor(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, n_layer=3):
        super(Predictor, self).__init__()
        layers = []
        current_dim = hidden_dim

        # Add the first layer
        layers.append(torch.nn.Linear(input_dim, current_dim))
        layers.append(torch.nn.LayerNorm(current_dim))
        layers.append(torch.nn.ReLU())

        # Add intermediate layers
        for _ in range(n_layer - 1):
            next_dim = max(current_dim // 2, output_dim)  # Ensure it doesn't drop below output_dim
            layers.append(torch.nn.Linear(current_dim, next_dim))
            layers.append(torch.nn.LayerNorm(next_dim))
            layers.append(torch.nn.ReLU())
            current_dim = next_dim

        # Add the final layer
        layers.append(torch.nn.Linear(current_dim, output_dim))

        # Combine layers into a sequential module
        self.NeuCF = torch.nn.Sequential(*layers)

    def forward(self, x):
        return self.NeuCF(x)

