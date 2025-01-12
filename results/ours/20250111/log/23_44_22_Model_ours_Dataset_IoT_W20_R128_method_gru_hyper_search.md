```python
|2025-01-11 23:44:22| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b82fcfd8bf0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 23:44:22| ********************Experiment Start********************
|2025-01-11 23:55:31| Round=1 BestEpoch=119 Acc=0.9286 F1=0.8908 Precision=0.8902 Recall=0.8918 Training_time=481.7 s 

|2025-01-11 23:55:31| ********************Experiment Results:********************
|2025-01-11 23:55:31| Acc: 0.9286 ± 0.0000
|2025-01-11 23:55:31| F1: 0.8908 ± 0.0000
|2025-01-11 23:55:31| P: 0.8902 ± 0.0000
|2025-01-11 23:55:31| Recall: 0.8918 ± 0.0000
|2025-01-11 23:55:31| train_time: 481.7000 ± 0.0000
|2025-01-11 23:55:31| Skip the efficiency calculation
|2025-01-11 23:55:32| ********************Experiment Success********************
```

