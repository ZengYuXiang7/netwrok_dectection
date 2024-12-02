# coding : utf-8
# Author : yuxiang Zeng

from default_config import *
from dataclasses import dataclass


@dataclass
class TestConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'ours'
    bs: int = 128
    rank: int = 30
    density: float = 0.3
    device: str = 'cpu'
    epochs: int = 250
    patience: int = 45
    classification: bool = True
    debug: bool = False
    window_size: int = 10
