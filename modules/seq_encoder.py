
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

        self.dropout = torch.nn.Dropout(0.1)
        self.MLP1 = torch.nn.Sequential(
            torch.nn.Linear(self.rank, self.rank),
            torch.nn.GELU(),
            torch.nn.Linear(self.rank, self.rank)
        )
        self.seq_output_norm1 = torch.nn.LayerNorm(self.rank)
        self.seq_output_norm2 = torch.nn.LayerNorm(self.rank)

    def forward(self, seq_embeds):
        if self.config.seq_method == 'lstm':
            seq_enc, (_, _) = self.lstm(seq_embeds)
        elif self.config.seq_method == 'gru':
            if self.bidirectional:
                seq_enc, _ = self.gru(seq_embeds)
            else:
                seq_enc, (_, _) = self.gru(seq_embeds)
        elif self.config.seq_method == 'self':
            seq_enc, _ = self.self_attention(seq_embeds, seq_embeds, seq_embeds)
        elif self.config.seq_method == 'external':
            seq_enc = self.external_attention(seq_embeds)

        if self.bidirectional:
            seq_enc = self.aggregator(seq_enc)

        seq_enc = seq_embeds + self.dropout(seq_enc)
        seq_enc = self.seq_output_norm1(seq_enc)
        seq_enc = seq_enc + self.dropout(self.MLP1(seq_enc))
        seq_enc = self.seq_output_norm2(seq_enc)
        
        return seq_enc