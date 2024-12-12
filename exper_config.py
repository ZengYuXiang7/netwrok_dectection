# coding : utf-8
# Author : yuxiang Zeng

from default_config import *
from dataclasses import dataclass


@dataclass
class TestConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'ours'
    bs: int = 128
    rank: int = 30
    density: float = 0.8
    device: str = 'cuda'
    epochs: int = 1000
    patience: int = 50
    classification: bool = True
    debug: bool = False
    window_size: int = 10
