```python
|2025-01-11 22:29:36| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7bc4058d2b10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 22:29:36| ********************Experiment Start********************
|2025-01-11 22:44:21| Round=1 BestEpoch=163 Acc=0.9266 F1=0.8909 Precision=0.8913 Recall=0.8910 Training_time=665.1 s 

|2025-01-11 22:44:21| ********************Experiment Results:********************
|2025-01-11 22:44:21| Acc: 0.9266 ± 0.0000
|2025-01-11 22:44:21| F1: 0.8909 ± 0.0000
|2025-01-11 22:44:21| P: 0.8913 ± 0.0000
|2025-01-11 22:44:21| Recall: 0.8910 ± 0.0000
|2025-01-11 22:44:21| train_time: 665.1217 ± 0.0000
|2025-01-11 22:44:22| Skip the efficiency calculation
|2025-01-11 22:44:22| ********************Experiment Success********************
```

