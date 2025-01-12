# coding : utf-8
# Author : yuxiang Zeng

from default_config import *
from dataclasses import dataclass

all_batch_size = 128

@dataclass
class TestConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'ours'
    bs: int = all_batch_size
    rank: int = 50
    density: float = 0.8
    device: str = 'cuda'
    epochs: int = 500
    patience: int = 30
    flow_length_limit: int = 20
    bidirectional: bool = True
    num_layers: int = 3



@dataclass
class MLPConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'mlp'
    bs: int = all_batch_size
    rank: int = 40
    epochs: int = 500
    patience: int = 30
    flow_length_limit: int = 20


@dataclass
class LSTMConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'lstm'
    bs: int = all_batch_size
    rank: int = 40
    epochs: int = 500
    patience: int = 30
    flow_length_limit: int = 20



@dataclass
class CNNConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'cnn'
    bs: int = all_batch_size
    rank: int = 40
    epochs: int = 500
    patience: int = 30
    flow_length_limit: int = 20


@dataclass
class GCNConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'gnn'
    bs: int = 64
    rank: int = 64
    epochs: int = 500
    patience: int = 30
    verbose: int = 10
    flow_length_limit: int = 20
    graph_encoder: str = 'gcn'
    order: int = 3

@dataclass
class GATConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'gnn'
    bs: int = 64
    rank: int = 64
    epochs: int = 500
    patience: int = 30
    verbose: int = 10
    flow_length_limit: int = 20
    graph_encoder: str = 'gat'
    order: int = 3
    heads: int = 2

@dataclass
class GINConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'gnn'
    bs: int = 64
    rank: int = 64
    epochs: int = 500
    patience: int = 30
    verbose: int = 10
    flow_length_limit: int = 20
    graph_encoder: str = 'gin'
    order: int = 3

@dataclass
class DAPPConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'dapp'
    bs: int = 150
    rank: int = 64
    epochs: int = 500
    patience: int = 30
    verbose: int = 10
    flow_length_limit: int = 20


@dataclass
class GraphIoTConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'graphiot'
    rank: int = 64
    epochs: int = 500
    patience: int = 30
    verbose: int = 10
    bs: int = 64
    flow_length_limit: int = 20