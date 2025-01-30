import torch
import math

class PositionalEmbedding(torch.nn.Module):
    def __init__(self, d_model, max_len=5000):
        super(PositionalEmbedding, self).__init__()
        # Compute the positional encodings once in log space.
        pe = torch.zeros(max_len, d_model).float()
        pe.require_grad = False

        position = torch.arange(0, max_len).float().unsqueeze(1)
        div_term = (torch.arange(0, d_model, 2).float() * -(math.log(10000.0) / d_model)).exp()
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)

        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)

    def forward(self, x):
        return self.pe[:, :x.size(1)]

class TokenEmbedding(torch.nn.Module):
    def __init__(self, c_in, d_model):
        super(TokenEmbedding, self).__init__()
        padding = 1 if torch.__version__ >= '1.5.0' else 2
        self.tokenConv = torch.nn.Conv1d(in_channels=c_in, out_channels=d_model,
                                   kernel_size=3, padding=padding, padding_mode='circular', bias=False)
        for m in self.modules():
            if isinstance(m, torch.nn.Conv1d):
                torch.nn.init.kaiming_normal_(m.weight, mode='fan_in', nonlinearity='leaky_relu')

    def forward(self, x):
        x = self.tokenConv(x.permute(0, 2, 1)).transpose(1, 2)
        return x

class DataEmbedding(torch.nn.Module):
    def __init__(self, c_in, d_model, config, dropout=0.1):
        super(DataEmbedding, self).__init__()
        self.config = config
        self.value_embedding = TokenEmbedding(c_in=c_in, d_model=d_model)  #(batch_size, len batch_x[1], d_model )
        self.position_embedding = PositionalEmbedding(d_model=d_model)  #(1,          len batch_x[1], d_model)
        self.dropout = torch.nn.Dropout(p=dropout)

    def forward(self, x):
        x = x.unsqueeze(-1)
        # print(x.shape)
        # if self.config.try_exp in [1, 3]:
        x = self.value_embedding(x) + self.position_embedding(x)
        # x = self.value_embedding(x)
        # elif self.config.try_exp in [2, 4]:
        # x = torch.permute(x, [0, 2, 1])
        # print(x.shape)
        # exit()
        return self.dropout(x)