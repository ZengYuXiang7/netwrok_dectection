# coding : utf-8
# Author : yuxiang Zeng

from default_config import *
from dataclasses import dataclass


@dataclass
class TestConfig(ExperimentConfig, BaseModelConfig, LoggerConfig, DatasetInfo, TrainingConfig, OtherConfig):
    model: str = 'ours'
    rank: int = 512
    density: float = 0.3
    bs: int = 128
    device: str = 'cpu'
    epochs: int = 250
    patience: int = 45
    classification: bool = True
    verbose: int = 1
    debug: bool = True
