```python
|2025-01-11 21:29:44| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7ad97f392630>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 128, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': gru, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 21:29:44| ********************Experiment Start********************
|2025-01-11 21:42:56| Round=1 BestEpoch=143 Acc=0.9274 F1=0.8901 Precision=0.8891 Recall=0.8915 Training_time=583.4 s 

|2025-01-11 21:42:56| ********************Experiment Results:********************
|2025-01-11 21:42:56| Acc: 0.9274 ± 0.0000
|2025-01-11 21:42:56| F1: 0.8901 ± 0.0000
|2025-01-11 21:42:56| P: 0.8891 ± 0.0000
|2025-01-11 21:42:56| Recall: 0.8915 ± 0.0000
|2025-01-11 21:42:56| train_time: 583.4374 ± 0.0000
|2025-01-11 21:42:57| Skip the efficiency calculation
|2025-01-11 21:42:57| ********************Experiment Success********************
```

