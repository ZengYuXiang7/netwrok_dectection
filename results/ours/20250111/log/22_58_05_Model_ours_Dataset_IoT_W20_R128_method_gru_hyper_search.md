```python
|2025-01-11 22:58:05| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e5279baab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 4, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 22:58:05| ********************Experiment Start********************
|2025-01-11 23:18:27| Round=1 BestEpoch=178 Acc=0.9276 F1=0.8919 Precision=0.8928 Recall=0.8914 Training_time=953.2 s 

|2025-01-11 23:18:27| ********************Experiment Results:********************
|2025-01-11 23:18:27| Acc: 0.9276 ± 0.0000
|2025-01-11 23:18:27| F1: 0.8919 ± 0.0000
|2025-01-11 23:18:27| P: 0.8928 ± 0.0000
|2025-01-11 23:18:27| Recall: 0.8914 ± 0.0000
|2025-01-11 23:18:27| train_time: 953.1534 ± 0.0000
|2025-01-11 23:18:28| Skip the efficiency calculation
|2025-01-11 23:18:29| ********************Experiment Success********************
```

