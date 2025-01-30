# coding : utf-8
# Author : yuxiang Zeng

from default_config import *
from dataclasses import dataclass

all_batch_size = 128

@dataclass
class TestConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'ours'
    bs: int = all_batch_size
    rank: int = 64
    density: float = 0.8
    device: str = 'cuda'
    epochs: int = 500
    patience: int = 60
    verbose: int = 1
    flow_length_limit: int = 30
    seq_method: str = 'gru'
    bidirectional: bool = True
    num_layers: int = 2
    n_heads:int = 4
    try_exp: int = 1



@dataclass
class MLPConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'mlp'
    bs: int = all_batch_size
    rank: int = 40
    epochs: int = 500
    patience: int = 30
    flow_length_limit: int = 30


@dataclass
class LSTMConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'lstm'
    bs: int = all_batch_size
    rank: int = 40
    epochs: int = 500
    patience: int = 30
    flow_length_limit: int = 30



@dataclass
class CNNConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'cnn'
    bs: int = all_batch_size
    rank: int = 40
    epochs: int = 500
    patience: int = 30
    flow_length_limit: int = 30


@dataclass
class GCNConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'gnn'
    bs: int = 64
    rank: int = 64
    epochs: int = 500
    patience: int = 30
    verbose: int = 10
    flow_length_limit: int = 30
    graph_encoder: str = 'gcn'
    order: int = 3
    rounds: int = 1


@dataclass
class GATConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'gnn'
    bs: int = 64
    rank: int = 64
    epochs: int = 500
    patience: int = 30
    verbose: int = 10
    flow_length_limit: int = 30
    graph_encoder: str = 'gat'
    order: int = 3
    heads: int = 2
    rounds: int = 1


@dataclass
class GINConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'gnn'
    bs: int = 64
    rank: int = 50
    epochs: int = 500
    patience: int = 30
    verbose: int = 10
    flow_length_limit: int = 30
    graph_encoder: str = 'gin'
    order: int = 2

@dataclass
class DAPPConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'dapp'
    bs: int = 150
    rank: int = 64
    epochs: int = 500
    patience: int = 30
    verbose: int = 10
    flow_length_limit: int = 30
    order: int = 2



@dataclass
class GraphIoTConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'graphiot'
    rank: int = 64
    epochs: int = 500
    patience: int = 30
    verbose: int = 10
    bs: int = 64
    flow_length_limit: int = 30
    lr: float = 0.0025

@dataclass
class StatisticsConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'stat'
    rank: int = 64
    epochs: int = 500
    patience: int = 30
    verbose: int = 10
    bs: int = 64
    flow_length_limit: int = 30