import torch
import dgl
import torch.nn as nn
from dgl.nn.pytorch import GINConv
import pickle

class MLP(torch.nn.Module):
    def __init__(self,in_feats,out_feats):
        super(MLP,self).__init__()
        self.linear_layers = torch.nn.ModuleList()
        self.layer = torch.nn.Sequential(
            torch.nn.Linear(in_features=in_feats, out_features=out_feats),
            torch.nn.Dropout(p=0.025),
            torch.nn.ReLU(),
            torch.nn.BatchNorm1d(out_feats),
            torch.nn.Linear(in_features=in_feats, out_features=out_feats),
            torch.nn.Dropout(p=0.025),
            torch.nn.ReLU(),
            torch.nn.BatchNorm1d(out_feats),
            torch.nn.Linear(in_features=in_feats, out_features=out_feats),
            torch.nn.Dropout(p=0.025),
            torch.nn.ReLU(),
            torch.nn.BatchNorm1d(out_feats),
        )


    def forward(self, x):
        return self.layer(x)


class GraphIoT(torch.nn.Module):
    def __init__(self, config):
        super(GraphIoT, self).__init__()
        self.config = config
        # 从配置文件加载信息
        with open(f'./datasets/flow/{config.dataset}_info_{config.flow_length_limit}.pickle', 'rb') as f:
            info = pickle.load(f)
            self.max_flow_length = info['max_flow_length']  # 输入流的最大长度
            num_classes = info['num_classes']  # 分类的类别数
        self.rank = config.rank
        self.order = 3
        self.seq_encoder = torch.nn.Linear(1, self.rank)
        self.layers = torch.nn.ModuleList(
            [dgl.nn.pytorch.GINConv(MLP(self.rank, self.rank), 'sum') for _ in range(self.order)]
        )
        self.classifier = torch.nn.Linear(self.rank * self.order, num_classes)

        if config.stat:
            self.feature_tf = torch.nn.Linear(39, config.rank)
            self.graph_tf = torch.nn.Linear(self.rank * self.order, self.rank)
            self.classifier = torch.nn.Linear(self.rank * 2, num_classes)  # 全连接层

    def forward(self, flow_feature, graph):
        feats = graph.ndata['feats'].reshape(-1, 1)
        bs = len(feats) // self.max_flow_length
        feats = self.seq_encoder(feats)
        all_graph_readout = []
        for i, layer in enumerate(self.layers):
            feats = layer(graph, feats)
            graph_readout = feats.reshape(bs, -1, self.rank)
            graph_readout = torch.sum(graph_readout, dim=1)
            all_graph_readout.append(graph_readout)
        all_graph_readout = torch.cat(all_graph_readout, dim=-1)

        if self.config.stat:
            feature_embeds = self.feature_tf(flow_feature)
            graph_embeds = self.graph_tf(all_graph_readout)
            final_input = torch.cat((graph_embeds, feature_embeds), 1)
            y = self.classifier(final_input)
        else:
            y = self.classifier(all_graph_readout)
        return y
