# coding : utf-8
# Author : Yuxiang Zeng
import torch


class DFT(torch.nn.Module):
    def __init__(self, config):
        super(DFT, self).__init__()
        self.config = config
        self.top_k = 5

    def forward(self, x):
        xf = torch.fft.rfft(x)
        freq = abs(xf)
        freq[0] = 0
        top_k_freq, top_list = torch.topk(freq, self.top_k)
        xf[freq <= top_k_freq.min()] = 0
        x_season = torch.fft.irfft(xf)
        x_trend = x - x_season
        return x_season, x_trend