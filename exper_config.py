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
    flow_length_limit: int = 30

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

