# coding : utf-8
# Author : yuxiang Zeng

from default_config import *
from dataclasses import dataclass


@dataclass
class TestConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'ours'
    bs: int = 64
    rank: int = 30
    density: float = 0.8
    device: str = 'cpu'
    epochs: int = 300
    patience: int = 20
    classification: bool = True
    debug: bool = False
    window_size: int = 10
