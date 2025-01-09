import torch
from torch import nn
from torch.nn import *

class ExternalAttention(torch.nn.Module):
    def __init__(self, d_model, S=64):
        super().__init__()
        self.mk = torch.nn.Linear(d_model, S, bias=False)
        self.mv = torch.nn.Linear(S, d_model, bias=False)
        self.softmax = torch.nn.Softmax(dim=1)
        self.init_weights()

    def init_weights(self):
        for m in self.modules():
            if isinstance(m, torch.nn.Conv2d):
                init.kaiming_normal_(m.weight, mode='fan_out')
                if m.bias is not None:
                    init.constant_(m.bias, 0)
            elif isinstance(m, torch.nn.BatchNorm2d):
                init.constant_(m.weight, 1)
                init.constant_(m.bias, 0)
            elif isinstance(m, torch.nn.Linear):
                init.normal_(m.weight, std=0.001)
                if m.bias is not None:
                    init.constant_(m.bias, 0)

    def forward(self, queries):
        queries = queries.to(torch.float32)
        attn = self.mk(queries)  # bs,n,S
        attn = self.softmax(attn)  # bs,n,S
        attn = attn / torch.sum(attn, dim=2, keepdim=True)  # bs,n,S
        out = self.mv(attn)  # bs,n,d_model
        return out