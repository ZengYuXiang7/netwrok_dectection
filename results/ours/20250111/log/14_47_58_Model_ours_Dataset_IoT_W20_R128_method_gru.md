```python
|2025-01-11 14:47:58| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x1409eee8ff50>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 128, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'seq_method': gru, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 14:47:58| ********************Experiment Start********************
|2025-01-11 14:48:00| Acc=0.9195 F1=0.8756 Precision=0.8741 Recall=0.8779 time=283.1 s 
|2025-01-11 14:48:00| ********************Experiment Results:********************
|2025-01-11 14:48:00| Acc: 0.9195 ± 0.0000
|2025-01-11 14:48:00| F1: 0.8756 ± 0.0000
|2025-01-11 14:48:00| P: 0.8741 ± 0.0000
|2025-01-11 14:48:00| Recall: 0.8779 ± 0.0000
|2025-01-11 14:48:00| train_time: 283.1455 ± 0.0000
|2025-01-11 14:48:02| Skip the efficiency calculation
|2025-01-11 14:48:02| ********************Experiment Success********************
```

