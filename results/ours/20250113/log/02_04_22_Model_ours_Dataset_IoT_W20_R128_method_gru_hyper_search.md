```python
|2025-01-13 02:04:22| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x758761cbdac0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 17, 'verbose': 10,
}
|2025-01-13 02:04:22| ********************Experiment Start********************
|2025-01-13 02:21:44| Round=1 BestEpoch=185 Acc=0.9275 F1=0.8921 Precision=0.8913 Recall=0.8938 Training_time=813.3 s 

|2025-01-13 02:21:44| ********************Experiment Results:********************
|2025-01-13 02:21:44| Acc: 0.9275 ± 0.0000
|2025-01-13 02:21:44| F1: 0.8921 ± 0.0000
|2025-01-13 02:21:44| P: 0.8913 ± 0.0000
|2025-01-13 02:21:44| Recall: 0.8938 ± 0.0000
|2025-01-13 02:21:44| train_time: 813.2750 ± 0.0000
|2025-01-13 02:21:45| Skip the efficiency calculation
|2025-01-13 02:21:45| ********************Experiment Success********************
```

