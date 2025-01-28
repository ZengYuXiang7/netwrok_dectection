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
        self.fragment_length = 10  # Length of each fragment (e.g., 5)
        self.step_size = 10  # Step size to move the sliding window (e.g., 5)

        self.patch_encoder = torch.nn.Sequential(
            *[SeqEncoder(1, config.rank, self.fragment_length, config.num_layers, config) for i in range(config.flow_length_limit // self.fragment_length)]
        )

        self.dropout = torch.nn.Dropout(0.10)
        self.att = torch.nn.MultiheadAttention(config.rank, config.n_heads, 0.10, batch_first=True)
        self.pos_embedding = torch.nn.Parameter(torch.randn(1, config.flow_length_limit // self.fragment_length + 1, config.rank))
        self.cls_token = torch.nn.Parameter(torch.randn(config.rank))

        self.fusion_layer = torch.nn.ModuleList()
        for i in range(len(self.patch_encoder)):
            self.fusion_layer.append(
                torch.nn.Linear(config.rank * 2, config.rank),
            )

        self.predictor = torch.nn.Sequential(
            torch.nn.LayerNorm(config.rank * 1),
            torch.nn.Linear(config.rank * 1, num_classes)
        )

    # def forward(self, time_interval, x):
    #     # 编码时间间隔与流序列
    #     # time_embeds = self.time_transfer(time_interval)
    #     # x = torch.abs(x)
    #     patch_embedding = []
    #     for i in range(len(self.scales)):
    #         now_x = x[:, ::self.scales[i]]
    #         patch_embedding.append(self.patch_encoder[i](now_x))
    #     x = torch.stack(patch_embedding, dim=1)
    #     x = torch.mean(x, dim=1)
    #     # softmax_weights = torch.nn.functional.softmax(x, dim=1)  # 在dim=1维度上应用softmax
    #     # x = softmax_weights * x  # 将 softmax 权重应用到原始的 x 上
    #     # x = torch.sum(x, dim=1)  # 聚合维度1上的加权和
    #     y = self.predictor(x)
    #     return y


    # def forward(self, time_interval, x):
    #     # if self.config.try_exp in [3, 4]:
    #     #     x = torch.abs(x)
    #     # x = self.enc_embedding(x)
    #     h_out = None
    #     for i in range(len(self.scales)):
    #         now_x = x[:, ::self.scales[i]]
    #         now_patch_embedding = self.patch_encoder[i](now_x)
    #         if i == 0:
    #             h_out = now_patch_embedding
    #         else:
    #             now_patch_embedding = torch.cat((now_patch_embedding, h_out), dim=-1)
    #             h_out = self.fusion_layer[i](now_patch_embedding)
    #     x = h_out
    #     y = self.predictor(x)
    #     return y

    # 这个想法是局部到总的融合。
    # def forward(self, _, x):
    #     fragments = []
    #
    #     for i in range(0, x.size(1), self.step_size):
    #         end = min(i + self.fragment_length, x.size(1))  # Ensure the fragment doesn't go out of bounds
    #         fragment = x[:, i:end]
    #         fragments.append(fragment)
    #
    #     fragment_embeddings = []
    #     all_embeddings = self.patch_encoder[-1](x)  # Process the entire input sequence with the last patch encoder
    #
    #     for i, fragment in enumerate(fragments):
    #         fragment_embedding = self.patch_encoder[i](fragment)  # Process with the corresponding patch encoder
    #         now_embedding = torch.cat([fragment_embedding, all_embeddings], dim=-1)
    #         fused_embedding = self.fusion_layer[i](now_embedding)  # Fusion with global x
    #         fragment_embeddings.append(fused_embedding)
    #     h_out = torch.stack(fragment_embeddings, dim=1)  # Sum aggregation of all the embeddings
    #     h_out = torch.mean(h_out, dim=1)
    #     y = self.predictor(h_out)
    #     return y

    # 尝试一下vit的思想，
    def forward(self, _, x):
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
        return y