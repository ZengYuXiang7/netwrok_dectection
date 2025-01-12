import torch
import dgl
from dgl.nn.pytorch import GINConv
import pickle

class DAPP(torch.nn.Module):
    def __init__(self, config):
        super(DAPP, self).__init__()
        self.config = config
        # 从配置文件加载信息
        with open(f'./datasets/flow/{config.dataset}_info_{config.flow_length_limit}.pickle', 'rb') as f:
            info = pickle.load(f)
            self.max_flow_length = info['max_flow_length']  # 输入流的最大长度
            num_classes = info['num_classes']  # 分类的类别数
        self.rank = config.rank
        self.order = 3
        self.seq_encoder = torch.nn.Linear(1, self.rank)
        self.layers = torch.nn.ModuleList([dgl.nn.pytorch.GINConv(torch.nn.Linear(self.rank, self.rank), 'sum')for _ in range(self.order)])
        self.linears = torch.nn.ModuleList([torch.nn.Linear(self.rank, self.rank) for _ in range(self.order)])
        self.norms = torch.nn.ModuleList([torch.nn.BatchNorm1d(self.rank) for _ in range(self.order)])
        self.acts = torch.nn.ModuleList([torch.nn.ReLU() for _ in range(self.order)])
        self.dropout = torch.nn.Dropout(0.05)
        self.classifier = torch.nn.Linear(self.rank * self.order, num_classes)

    def forward(self, graph, _, __):
        feats = graph.ndata['feats'].reshape(-1, 1)
        bs = len(feats) // self.max_flow_length
        feats = self.seq_encoder(feats)
        all_graph_readout = []
        for i, (layer, linear, norm, act) in enumerate(zip(self.layers, self.linears, self.norms, self.acts)):
            feats = layer(graph, feats)
            feats = linear(feats)
            feats = norm(feats)
            feats = self.dropout(feats)
            feats = act(feats)
            graph_readout = feats.reshape(bs, -1, self.rank)
            graph_readout = torch.sum(graph_readout, dim=1)
            all_graph_readout.append(graph_readout)
        all_graph_readout = torch.cat(all_graph_readout, dim=-1)
        y = self.classifier(all_graph_readout)
        return y
