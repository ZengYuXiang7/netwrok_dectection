# coding : utf-8
# Author : Yuxiang Zeng
import torch
import pickle
import dgl

class GnnFamily(torch.nn.Module):
    def __init__(self, config):
        super(GnnFamily, self).__init__()
        self.config = config
        # 从配置文件加载信息
        with open(f'./datasets/flow/{config.dataset}_info_{config.flow_length_limit}.pickle', 'rb') as f:
            info = pickle.load(f)
            self.max_flow_length = info['max_flow_length']  # 输入流的最大长度
            num_classes = info['num_classes']  # 分类的类别数
        self.rank = config.rank
        self.order = config.order
        self.seq_encoder = torch.nn.Linear(1, self.rank)
        if config.graph_encoder == 'gcn':
            self.layers = torch.nn.ModuleList([dgl.nn.pytorch.GraphConv(self.rank, self.rank) for i in range(self.order)])
        elif config.graph_encoder == 'graphsage':
            self.layers = torch.nn.ModuleList([dgl.nn.pytorch.SAGEConv(self.rank, self.rank, aggregator_type='gcn') for i in range(self.order)])
        elif config.graph_encoder == 'gat':
            self.layers = torch.nn.ModuleList([dgl.nn.pytorch.GATConv(self.rank, self.rank, config.heads, 0.10) for i in range(self.order)])
        elif config.graph_encoder == 'gin':
            self.layers = torch.nn.ModuleList([dgl.nn.pytorch.GINConv(torch.nn.Linear(self.rank, self.rank), 'sum')])
        else:
            raise NotImplementedError
        self.norms = torch.nn.ModuleList([torch.nn.LayerNorm(self.rank) for _ in range(self.order)])
        self.acts = torch.nn.ModuleList([torch.nn.ReLU() for _ in range(self.order)])
        self.dropout = torch.nn.Dropout(0.10)
        self.readout_layer = torch.nn.Linear(self.rank, self.rank)
        self.classifier = torch.nn.Linear(self.rank * self.max_flow_length, num_classes)

        if config.stat:
            self.feature_tf = torch.nn.Linear(39, config.rank)
            self.graph_tf = torch.nn.Linear(self.rank * self.max_flow_length, self.rank)
            self.classifier = torch.nn.Linear(self.rank * 2, num_classes)  # 全连接层

    def forward(self, flow_feature, graph):
        feats = graph.ndata['feats'].reshape(-1, 1)
        bs = len(feats) // self.max_flow_length
        feats = self.seq_encoder(feats)
        for i, (layer, norm, act) in enumerate(zip(self.layers, self.norms, self.acts)):
            feats = layer(graph, feats)
            if self.config.graph_encoder == 'gat':
                feats = feats.mean(dim=1)  # 聚合多个头的输出
            feats = norm(feats)
            feats = act(feats)
            if self.config.graph_encoder != 'gat':
                feats = self.dropout(feats)
        # feats = feats.reshape(bs, -1, self.rank)
        # feats = torch.mean(feats, dim=1)
        feats = feats.reshape(bs, -1)

        if self.config.stat:
            feature_embeds = self.feature_tf(flow_feature)
            graph_embeds = self.graph_tf(feats)
            final_input = torch.cat((graph_embeds, feature_embeds), 1)
            y = self.classifier(final_input)
        else:
            y = self.classifier(feats)
        return y



def construct_edge_features(graph, src, dst, timestamp, config):
    graph.add_edges(src, dst)
    if config.model == 'graphiot':
        if abs(timestamp[src] - timestamp[dst]) > 1:
            graph.edges[src, dst].data['edge_feats'] = torch.tensor([0.01])
        else:
            graph.edges[src, dst].data['edge_feats'] = torch.tensor([1.0])
    return graph


def build_single_graph(seq, timestamp, config):
    """
    根据序列构建自定义图，每个点对应一个节点，并根据方向添加边。

    :param seq: 一维张量，表示序列中的值。
    :return: DGL 图对象。
    """
    num_nodes = len(seq)
    # 创建一个空图，并预先指定节点数量
    graph = dgl.graph([])
    graph = dgl.add_nodes(graph, num_nodes)

    previous_direction = 1

    for i in range(num_nodes):
        current_value = seq[i].item()
        current_direction = 1 if current_value > 0 else -1  # 当前方向
        if current_direction == previous_direction:
            if i == 0:
                continue
            # graph = construct_edge_features(graph, i, i - 1, timestamp, config)
            graph = construct_edge_features(graph, i - 1, i, timestamp, config)
            # graph.add_edges(i, i - 1)
            # graph.add_edges(i - 1, i)
            # print(f"无向边 连边 {i - 1} -- {i}")
        else:
            if i == 1:
                graph = construct_edge_features(graph, 0, i, timestamp, config)
                # graph.add_edges(0, i)
                # print(f"连边 {0} -- {i}")
                previous_direction = current_direction
                continue
            # 如果方向还是相反就找号最小的那个点相连
            for j in range(i - 1, -1, -1):
                # print(j, i)
                now_direction = 1 if seq[j].item() > 0 else -1
                if now_direction != current_direction:
                    # print(f'i={i}还没找到最小号节点j={j}，继续找')
                    pass
                else:
                    # 直到找到号最小的那个
                    graph = construct_edge_features(graph, j + 1, i, timestamp, config)
                    # graph.add_edges(j + 1, i)
                    # print(f"连边 {j + 1} -- {i}")
                    break
            # print('12313')
        if i + 1 < num_nodes:
            next_direction = 1 if seq[i + 1].item() > 0 else -1
            if current_direction != next_direction:
                # print(f'{i} - {i + 1}方向不同')
                # 如果方向不同, 最大号的节点与前一反方向最大号节点相连
                for j in range(i - 1, -1, -1):
                    now_direction = 1 if seq[j].item() > 0 else -1
                    if now_direction == current_direction:
                        continue
                    else:
                        graph = construct_edge_features(graph, j, i, timestamp, config)
                        # graph.add_edges(j, i)
                        # print(f"+ 连边 {j} -- {i}")
                        break
            else:
                # print(f'{i} - {i + 1}方向相同，跳过')
                pass
        previous_direction = current_direction
    graph = dgl.add_self_loop(graph)
    graph.ndata['feats'] = seq
    return graph