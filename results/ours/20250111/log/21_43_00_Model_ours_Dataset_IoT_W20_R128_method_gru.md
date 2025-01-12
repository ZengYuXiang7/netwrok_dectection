```python
|2025-01-11 21:43:00| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xf8ee4c5eb70>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 21:43:00| ********************Experiment Start********************
|2025-01-11 21:43:02| Acc=0.9251 F1=0.8879 Precision=0.8867 Recall=0.8895 time=583.4 s 
|2025-01-11 21:43:02| ********************Experiment Results:********************
|2025-01-11 21:43:02| Acc: 0.9251 ± 0.0000
|2025-01-11 21:43:02| F1: 0.8879 ± 0.0000
|2025-01-11 21:43:02| P: 0.8867 ± 0.0000
|2025-01-11 21:43:02| Recall: 0.8895 ± 0.0000
|2025-01-11 21:43:02| train_time: 583.4374 ± 0.0000
|2025-01-11 21:43:05| Skip the efficiency calculation
|2025-01-11 21:43:05| ********************Experiment Success********************
```

