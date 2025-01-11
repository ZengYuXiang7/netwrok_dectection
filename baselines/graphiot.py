import torch
import dgl
import torch.nn as nn
from dgl.nn.pytorch import GINConv
import pickle

# https://github.com/jmhIcoding/traffic_classification_utils/blob/main/models/dl/graphDapp/DApp_Classifier.py
class DApp_MLP(nn.Module):
    def __init__(self,in_feats, out_feats=64, layer_nums = 3):
        super(DApp_MLP,self).__init__()
        self.linear_layers =nn.ModuleList()
        for each in range(layer_nums):
            if each == 0 :
                in_features= in_feats
            else:
                in_features = out_feats
            self.linear_layers.append(nn.Linear(in_features= in_features,out_features=out_feats))
        self.activate = nn.ReLU()
        self.batchnorm = nn.BatchNorm1d(out_feats)
        self.dropout = nn.Dropout(p=0.0)

    def forward(self, x):
        x1 = x
        for mod in self.linear_layers :
            x1 = mod(x1)
            x1 = self.activate(x1)
        x2 = self.batchnorm(x1)
        x3 = self.dropout(x2)
        return x3

class DApp(nn.Module):
    def __init__(self, config, gin_layer_num=3, gin_hidden_units=64, iteration_nums = 3, graph_pooling_type='sum',
                 neighbor_pooling_type='sum', iteration_first=True, embedding= True):
        #DApp: 3个GIN,顺序级联在一起
        super(DApp,self).__init__()
        self.config = config
        with open(f'./datasets/flow/{config.dataset}_info_{config.flow_length_limit}.pickle', 'rb') as f:
            info = pickle.load(f)
            self.max_flow_length = info['max_flow_length']  # 输入流的最大长度
            num_classes = info['num_classes']  # 分类的类别数
            self.gin_layer_num = gin_layer_num
            self.gin_hidden_uints = gin_hidden_units
            self.iteration_nums = iteration_nums
            self.graph_pooling_type = graph_pooling_type
            self.neighbor_pooling_type= neighbor_pooling_type
            self.gin_layers = []
            self.interation_first = iteration_first
            self.embedding = embedding
            self.embedding_dim = gin_hidden_units      #embedding的设置为gin的隐藏神经元个数
        self.embedding_layer = torch.nn.Embedding(num_embeddings=3100, embedding_dim=self.embedding_dim)
        for each in range(gin_layer_num):
            if each == 0:
                in_feats = self.embedding_dim if self.embedding == True else 1
            else:
                in_feats = gin_hidden_units
            mlp = DApp_MLP(in_feats, out_feats= gin_hidden_units, layer_nums= self.gin_layer_num)
            gin_layer = GINConv(apply_func= mlp, aggregator_type=self.neighbor_pooling_type, learn_eps=True).to(self.config.device)
            self.gin_layers.append(gin_layer)
        self.linear = nn.Linear(in_features=iteration_nums * gin_hidden_units,out_features=num_classes)

    def forward(self, graph, _, __):
        node_feature = graph.ndata['feats'].to(self.config.device)
        node_feature = self.embedding_layer(torch.reshape(node_feature.long(), (-1,)) + 1500)
        graph_feature_history = []
        for layer in self.gin_layers:
            node_feature = layer(graph, node_feature)
            graph.ndata['iterated_feature'] = node_feature
            if self.graph_pooling_type == 'sum':
                graph_feature = dgl.sum_nodes(graph,'iterated_feature')
            elif self.graph_pooling_type == 'mean':
                graph_feature = dgl.mean_nodes(graph,'iterated_feature')
            graph_feature_history.append(graph_feature)
        graph_features = torch.cat(graph_feature_history,-1)
        y = self.linear(graph_features)
        return  y
