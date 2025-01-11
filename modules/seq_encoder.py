
import torch
from modules.attention import ExternalAttention


class SeqEncoder(torch.nn.Module):
    def __init__(self, config):
        super(SeqEncoder, self).__init__()
        self.config = config
        self.rank = config.rank
        self.bidirectional = config.bidirectional
        if self.config.seq_method == 'lstm':
            self.lstm = torch.nn.LSTM(self.rank, self.rank, num_layers=2, bias=True, batch_first=True, dropout=0.05, bidirectional=self.bidirectional)
        elif self.config.seq_method == 'gru':
            self.gru = torch.nn.GRU(self.rank, self.rank, num_layers=2, bias=True, batch_first=True, dropout=0.05, bidirectional=self.bidirectional)
        elif self.config.seq_method == 'self':
            self.self_attention = torch.nn.MultiheadAttention(self.rank, 4, 0.10, batch_first=True)
        elif self.config.seq_method == 'external':
            self.external_attention = ExternalAttention(self.rank, 128)
        if self.bidirectional:
            self.aggregator = torch.nn.Linear(self.rank * 2, self.rank)

    def forward(self, seq_embeds):
        if self.config.seq_method == 'lstm':
            seq_output, (_, _) = self.lstm(seq_embeds)
        elif self.config.seq_method == 'gru':
            if self.bidirectional:
                seq_output, _ = self.gru(seq_embeds)
            else:
                seq_output, (_, _) = self.gru(seq_embeds)
        elif self.config.seq_method == 'self':
            seq_output, _ = self.self_attention(seq_embeds, seq_embeds, seq_embeds)
        elif self.config.seq_method == 'external':
            seq_output = self.external_attention(seq_embeds)

        if self.bidirectional:
            seq_output = self.aggregator(seq_output)
        return seq_output