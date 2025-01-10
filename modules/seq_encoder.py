
import torch
from modules.attention import ExternalAttention


class SeqEncoder(torch.nn.Module):
    def __init__(self, config):
        super(SeqEncoder, self).__init__()
        self.config = config
        self.rank = config.rank
        if self.config.seq_method == 'lstm':
            self.lstm = torch.nn.LSTM(self.rank, self.rank, num_layers=2, bias=True, batch_first=True, dropout=0.05, bidirectional=False)
        elif self.config.seq_method == 'gru':
            self.gru = torch.nn.GRU(self.rank, self.rank, num_layers=2, bias=True, batch_first=True, dropout=0.05)
        elif self.config.seq_method == 'self':
            self.self_attention = torch.nn.MultiheadAttention(self.rank, 4, 0.10, batch_first=True)
        elif self.config.seq_method == 'external':
            self.external_attention = ExternalAttention(self.rank, 128)

    def forward(self, seq_embeds):
        if self.config.seq_method == 'lstm':
            seq_output, (_, _) = self.lstm(seq_embeds)
        elif self.config.seq_method == 'gru':
            seq_output, (_, _) = self.gru(seq_embeds)
        elif self.config.seq_method == 'self':
            seq_output, _ = self.self_attention(seq_embeds, seq_embeds, seq_embeds)
        elif self.config.seq_method == 'external':
            seq_output = self.external_attention(seq_embeds)
        return seq_output