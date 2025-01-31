# coding : utf-8
# Author : Yuxiang Zeng
from typing import final

import torch

from modules.attention import ExternalAttention
from modules.dft import DFT
from modules.position_encoding import DataEmbedding
from modules.predictor import Predictor, Predictor2
import pickle
from einops import rearrange, repeat, pack, unpack
from einops.layers.torch import Rearrange
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

        # Flow encoder
        if self.config.ablation == 1:
            self.fragment_length = config.flow_length_limit  # Length of each fragment (e.g., 5)
            self.step_size = config.flow_length_limit  # Step size to move the sliding window (e.g., 5)
            self.fc = torch.nn.Linear(1, config.rank)
            self.patch_encoder = torch.nn.Sequential(
                *[torch.nn.LSTM(config.rank, config.rank) for i in range(config.flow_length_limit // self.fragment_length)]
            )

            self.predictor = torch.nn.Sequential(
                torch.nn.LayerNorm(config.rank * self.step_size),
                torch.nn.Linear(config.rank * self.step_size, num_classes)
            )
        elif self.config.ablation == 2:
            config.num_layers = 1
            self.fragment_length = config.flow_length_limit  # Length of each fragment (e.g., 5)
            self.step_size = config.flow_length_limit  # Step size to move the sliding window (e.g., 5)

            self.patch_encoder = torch.nn.Sequential(
                *[SeqEncoder(1, config.rank, self.fragment_length, config.num_layers, config) for i in
                  range(config.flow_length_limit // self.fragment_length)]
            )

            self.predictor = torch.nn.Sequential(
                torch.nn.LayerNorm(config.rank * 1),
                torch.nn.Linear(config.rank * 1, num_classes)
            )
        elif self.config.ablation == 3:
            config.num_layers = 1
            self.fragment_length = 10  # Length of each fragment (e.g., 5)
            self.step_size = 10  # Step size to move the sliding window (e.g., 5)
            self.fc = torch.nn.Linear(1, config.rank)
            self.patch_encoder = torch.nn.Sequential(
                *[torch.nn.GRU(config.rank, config.rank) for i in range(config.flow_length_limit // self.fragment_length)]
            )
            self.patch_fc = torch.nn.Linear(config.rank * self.step_size, self.config.rank)

            self.dropout = torch.nn.Dropout(0.10)
            self.att = torch.nn.MultiheadAttention(config.rank, config.n_heads, 0.10, batch_first=True)
            self.pos_embedding = torch.nn.Parameter(
                torch.randn(1, config.flow_length_limit // self.fragment_length + 1, config.rank))
            self.cls_token = torch.nn.Parameter(torch.randn(config.rank))

            self.predictor = torch.nn.Sequential(
                torch.nn.LayerNorm(config.rank * 1),
                torch.nn.Linear(config.rank * 1, num_classes)
            )
        else:
            self.fragment_length = 10  # Length of each fragment (e.g., 5)
            self.step_size = 10  # Step size to move the sliding window (e.g., 5)

            self.patch_encoder = torch.nn.ModuleList(
                [SeqEncoder(1, config.rank, self.fragment_length, config.num_layers, config) for i in range(config.flow_length_limit // self.fragment_length)]
            )

            self.dropout = torch.nn.Dropout(0.10)
            self.att = torch.nn.MultiheadAttention(config.rank, config.n_heads, 0.10, batch_first=True)
            self.pos_embedding = torch.nn.Parameter(torch.randn(1, config.flow_length_limit // self.fragment_length + 1, config.rank))
            self.cls_token = torch.nn.Parameter(torch.randn(config.rank))

            self.predictor = torch.nn.Sequential(
                torch.nn.LayerNorm(config.rank * 1),
                torch.nn.Linear(config.rank * 1, num_classes)
            )

    def forward(self, flow_feature, x):
        if self.config.ablation == 0:
            # print(x.max(), x.min())
            # x = torch.abs(x)
            b, n = x.shape
            fragments = []
            for i in range(0, x.size(1), self.step_size):
                end = min(i + self.fragment_length, x.size(1))  # Ensure the fragment doesn't go out of bounds
                fragment = x[:, i:end]
                fragments.append(fragment)

            fragment_embeddings = []
            for i, fragment in enumerate(fragments):
                fragment_embedding = self.patch_encoder[i](fragment)  # Process with the corresponding patch encoder
                fragment_embeddings.append(fragment_embedding)
            x = torch.stack(fragment_embeddings, dim=1)  # Sum aggregation of all the embeddings
            cls_tokens = repeat(self.cls_token, 'd -> b d', b=b)
            x, ps = pack([cls_tokens, x], 'b * d')
            x += self.pos_embedding[:, :(n + 1)]
            x = self.dropout(x)
            x, _ = self.att(x, x, x)
            cls_tokens, _ = unpack(x, ps, 'b * d')
            y = self.predictor(cls_tokens)
        elif self.config.ablation == 1:
            x = x.unsqueeze(-1)
            x = self.fc(x)
            x, _ = self.patch_encoder(x)
            x = x.reshape(x.size(0), -1)
            y = self.predictor(x)
        elif self.config.ablation == 2:
            x = self.patch_encoder(x)
            y = self.predictor(x)
        elif self.config.ablation == 3:
            b, n = x.shape
            fragments = []
            for i in range(0, x.size(1), self.step_size):
                end = min(i + self.fragment_length, x.size(1))  # Ensure the fragment doesn't go out of bounds
                fragment = x[:, i:end]
                fragments.append(fragment)

            fragment_embeddings = []
            for i, fragment in enumerate(fragments):
                fragment = fragment.unsqueeze(-1)
                fragment = self.fc(fragment)
                fragment_embedding, _ = self.patch_encoder[i](fragment)  # Process with the corresponding patch encoder
                fragment_embedding = self.patch_fc(fragment_embedding.reshape(fragment_embedding.size(0), -1))
                fragment_embeddings.append(fragment_embedding)
            x = torch.stack(fragment_embeddings, dim=1)  # Sum aggregation of all the embeddings
            cls_tokens = repeat(self.cls_token, 'd -> b d', b=b)
            x, ps = pack([cls_tokens, x], 'b * d')
            x += self.pos_embedding[:, :(n + 1)]
            x = self.dropout(x)
            x, _ = self.att(x, x, x)
            cls_tokens, _ = unpack(x, ps, 'b * d')
            y = self.predictor(cls_tokens)
        elif self.config.ablation == 4:
            b, n = x.shape
            fragments = []
            for i in range(0, x.size(1), self.step_size):
                end = min(i + self.fragment_length, x.size(1))  # Ensure the fragment doesn't go out of bounds
                fragment = x[:, i:end]
                fragments.append(fragment)

            fragment_embeddings = []
            for i, fragment in enumerate(fragments):
                fragment = fragment.unsqueeze(-1)
                fragment = self.fc(fragment)
                fragment_embedding, _ = self.patch_encoder[i](fragment)  # Process with the corresponding patch encoder
                fragment_embedding = self.patch_fc(fragment_embedding.reshape(fragment_embedding.size(0), -1))
                fragment_embeddings.append(fragment_embedding)
            x = torch.stack(fragment_embeddings, dim=1)  # Sum aggregation of all the embeddings
            cls_tokens = repeat(self.cls_token, 'd -> b d', b=b)
            x, ps = pack([cls_tokens, x], 'b * d')
            x += self.pos_embedding[:, :(n + 1)]
            x = self.dropout(x)
            x, _ = self.att(x, x, x)
            cls_tokens, _ = unpack(x, ps, 'b * d')
            y = self.predictor(cls_tokens)
        return y