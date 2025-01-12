```python
|2025-01-12 10:06:36| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x13dee8ae2b10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 4, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-12 10:06:36| ********************Experiment Start********************
|2025-01-12 10:06:38| Acc=0.9233 F1=0.8840 Precision=0.8834 Recall=0.8852 time=569.0 s 
|2025-01-12 10:06:38| ********************Experiment Results:********************
|2025-01-12 10:06:38| Acc: 0.9233 ± 0.0000
|2025-01-12 10:06:38| F1: 0.8840 ± 0.0000
|2025-01-12 10:06:38| P: 0.8834 ± 0.0000
|2025-01-12 10:06:38| Recall: 0.8852 ± 0.0000
|2025-01-12 10:06:38| train_time: 569.0133 ± 0.0000
|2025-01-12 10:06:40| Skip the efficiency calculation
|2025-01-12 10:06:40| ********************Experiment Success********************
```

