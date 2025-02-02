
import torch
from modules.attention import ExternalAttention
from modules.position_encoding import TokenEmbedding, PositionalEmbedding


class SeqLayer(torch.nn.Module):
    def __init__(self, d_model, config):
        super(SeqLayer, self).__init__()
        self.config = config
        self.bidirectional = config.bidirectional
        self.d_model = d_model

        # LSTM、GRU、Self-Attention、External Attention选择
        if config.seq_method == 'lstm':
            self.lstm = torch.nn.LSTM(self.d_model, self.d_model, num_layers=2, bias=True, batch_first=True, dropout=0.10,
                                      bidirectional=config.bidirectional)
        elif config.seq_method == 'gru':
            self.gru = torch.nn.GRU(self.d_model, self.d_model, num_layers=2, bias=True, batch_first=True, dropout=0.10,
                                    bidirectional=config.bidirectional)
        elif config.seq_method == 'self':
            self.self_attention = torch.nn.MultiheadAttention(self.d_model, 2, 0.10, batch_first=True)
        elif config.seq_method == 'external':
            self.external_attention = ExternalAttention(self.d_model, 128)
        # 新增的卷积序列处理方法
        elif config.seq_method == 'cnn':
            self.cnn = torch.nn.Conv1d(in_channels=self.d_model, out_channels=self.d_model, kernel_size=3, padding=1)
            self.cnn_activation = torch.nn.GELU()

        if config.bidirectional:
            self.aggregator = torch.nn.Linear(self.d_model * 2, self.d_model)

        self.MLP1 = torch.nn.Sequential(
            torch.nn.Linear(self.d_model, self.d_model),
            torch.nn.GELU(),
            torch.nn.Linear(self.d_model, self.d_model)
        )
        self.dropout = torch.nn.Dropout(0.1)
        self.seq_output_norm1 = torch.nn.LayerNorm(self.d_model)
        self.seq_output_norm2 = torch.nn.LayerNorm(self.d_model)

    def forward(self, seq_embeds):
        # 选择性处理不同类型的序列
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
        elif self.config.seq_method == 'cnn':
            seq_enc = seq_embeds.permute(0, 2, 1)  # 转换为 (batch_size, d_model, L)
            seq_enc = self.cnn(seq_enc)  # 卷积操作
            seq_enc = self.cnn_activation(seq_enc)  # 激活函数
            seq_enc = seq_enc.permute(0, 2, 1)  # 转回 (batch_size, L, d_model)

        # 如果是双向模型，将其聚合
        if self.bidirectional and self.config.seq_method in ['lstm', 'gru']:
            seq_enc = self.aggregator(seq_enc)

        # 残差连接 + Dropout
        seq_enc = seq_embeds + self.dropout(seq_enc)
        seq_enc = self.seq_output_norm1(seq_enc)
        seq_enc = seq_enc + self.dropout(self.MLP1(seq_enc))
        seq_enc = self.seq_output_norm2(seq_enc)

        return seq_enc


class SeqEncoder(torch.nn.Module):
    def __init__(self, input_size, d_model, seq_len, num_layers, config):
        super(SeqEncoder, self).__init__()
        self.config = config
        self.seq_transfer = torch.nn.Linear(input_size, d_model)
        self.position_embedding = PositionalEmbedding(d_model=d_model)  #(1,          len batch_x[1], d_model)
        self.seq_encoder = torch.nn.ModuleList(
            [SeqLayer(d_model, config) for _ in range(num_layers)]
        )
        self.aggregator = torch.nn.Linear(seq_len * d_model, d_model)


    def forward(self, x):
        x = x.unsqueeze(-1)
        x = self.seq_transfer(x)
        for i in range(self.config.num_layers):
            x = x + self.seq_encoder[i](x)
        x = x.reshape(x.shape[0], -1)
        x = self.aggregator(x)
        return x
