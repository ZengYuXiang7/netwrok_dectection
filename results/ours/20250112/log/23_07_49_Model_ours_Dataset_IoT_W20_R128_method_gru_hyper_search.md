```python
|2025-01-12 23:07:49| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b11c7ae8d70>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 3, 'verbose': 10,
}
|2025-01-12 23:07:49| ********************Experiment Start********************
|2025-01-12 23:19:59| Round=1 BestEpoch=133 Acc=0.9254 F1=0.8844 Precision=0.8834 Recall=0.8860 Training_time=536.2 s 

|2025-01-12 23:19:59| ********************Experiment Results:********************
|2025-01-12 23:19:59| Acc: 0.9254 ± 0.0000
|2025-01-12 23:19:59| F1: 0.8844 ± 0.0000
|2025-01-12 23:19:59| P: 0.8834 ± 0.0000
|2025-01-12 23:19:59| Recall: 0.8860 ± 0.0000
|2025-01-12 23:19:59| train_time: 536.1644 ± 0.0000
|2025-01-12 23:20:00| Skip the efficiency calculation
|2025-01-12 23:20:00| ********************Experiment Success********************
```

