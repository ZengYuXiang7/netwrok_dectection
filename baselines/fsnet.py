import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

class MultiBiGRU(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, dropout, is_train, is_cat=True):
        super(MultiBiGRU, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.dropout = dropout if is_train and num_layers > 1 else 0  # 仅在 num_layers > 1 时应用 dropout
        self.is_cat = is_cat

        # 创建多层双向 GRU
        self.grus = nn.ModuleList([
            nn.GRU(input_size if i == 0 else 2 * hidden_size, hidden_size, num_layers=1, bidirectional=True, dropout=self.dropout)
            for i in range(num_layers)
        ])

    def forward(self, inputs, seq_len):
        batch_size = inputs.size(0)
        max_len = inputs.size(1)
        hidden_size = self.hidden_size

        # 初始化隐藏状态
        h0 = torch.zeros(2, batch_size, hidden_size).to(inputs.device)

        outputs = [inputs]
        output_states = []
        for i, gru in enumerate(self.grus):
            # 打包变长序列
            packed_input = pack_padded_sequence(outputs[-1], seq_len, batch_first=True, enforce_sorted=False)
            # 通过 GRU
            packed_output, hn = gru(packed_input, h0)
            # 解包
            output, _ = pad_packed_sequence(packed_output, batch_first=True, total_length=max_len)
            outputs.append(output)
            output_states.append(hn)

        if self.is_cat:
            # 拼接所有层的输出
            res = torch.cat(outputs[1:], dim=2)
            res_state = torch.cat(output_states, dim=2)
        else:
            # 只使用最后一层的输出
            res = outputs[-1]
            res_state = output_states[-1]

        return res_state, res


class FSNet(nn.Module):
    def __init__(self, config):
        super(FSNet, self).__init__()
        self.config = config

        # 嵌入层
        self.embedding = nn.Embedding(config.length_num, config.length_dim)

        # 将嵌入后的特征维度转换为 hidden_size
        self.embedding_proj = nn.Linear(config.length_dim, config.hidden)

        # 编码器和解码器
        self.encoder = MultiBiGRU(config.hidden, config.hidden, config.layer, config.keep_prob, is_train=True)
        self.decoder = MultiBiGRU(config.hidden, config.hidden, config.layer, config.keep_prob, is_train=True)

        # 分类器
        self.classifier = nn.Linear(2 * config.hidden, config.class_num)

        # 重构层
        self.reconstruct = nn.Linear(config.hidden, config.length_num)

        # 特征融合
        self.fusion_gate = nn.Sequential(
            nn.Linear(4 * config.hidden, config.hidden),
            nn.Sigmoid()
        )
        self.fusion_update = nn.Sequential(
            nn.Linear(4 * config.hidden, config.hidden),
            nn.Tanh()
        )

        # 特征压缩
        self.compress = nn.Sequential(
            nn.Linear(4 * config.hidden, 2 * config.hidden),
            nn.SELU()
        )

    def forward(self, flow, seq_len):
        # 嵌入层
        seq = self.embedding(flow)  # (batch_size, seq_len, length_dim)

        # 将嵌入后的特征维度转换为 hidden_size
        seq = self.embedding_proj(seq)  # (batch_size, seq_len, hidden_size)

        # 编码器
        e_fea, in_output = self.encoder(seq, seq_len)

        # 解码器输入
        dec_input = e_fea.unsqueeze(1).repeat(1, seq.size(1), 1)

        # 解码器
        d_fea, l_output = self.decoder(dec_input, seq_len)

        # 重构损失
        rec_logits = self.reconstruct(l_output)
        rec_loss = F.cross_entropy(rec_logits.view(-1, self.config.length_num), flow.view(-1), reduction='none')
        rec_loss = (rec_loss * (flow != 0).float().view(-1)).sum() / (flow != 0).float().sum()

        # 特征融合
        fea = torch.cat([e_fea, d_fea, e_fea * d_fea], dim=1)
        g = self.fusion_gate(fea)
        update_ = self.fusion_update(fea)
        fused_fea = e_fea * g + (1 - g) * update_

        # 特征压缩
        compressed_fea = self.compress(fused_fea)

        # 分类
        logits = self.classifier(compressed_fea)
        pred = torch.argmax(logits, dim=1)
        c_loss = F.cross_entropy(logits, self.label)

        # 总损失
        loss = c_loss + self.config.rec_loss * rec_loss

        return loss, pred


# 示例配置
class Config:
    def __init__(self):
        self.batch_size = 32
        self.length_dim = 128
        self.length_num = 1000
        self.hidden = 256
        self.layer = 2
        self.keep_prob = 0.8
        self.class_num = 10
        self.rec_loss = 0.1


# 示例调用
config = Config()
model = FSNet(config)

# 假设输入数据
flow = torch.randint(0, config.length_num, (config.batch_size, 50))  # (batch_size, seq_len)
seq_len = torch.randint(10, 50, (config.batch_size,))  # 每个序列的实际长度
label = torch.randint(0, config.class_num, (config.batch_size,))  # 标签

# 前向传播
loss, pred = model(flow, seq_len)
print("Loss:", loss.item())
print("Predictions:", pred)