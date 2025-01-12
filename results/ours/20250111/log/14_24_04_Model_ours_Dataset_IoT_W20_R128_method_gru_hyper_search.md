```python
|2025-01-11 14:24:04| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x76b6c38be840>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 128, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': gru, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 14:24:04| ********************Experiment Start********************
|2025-01-11 14:25:54| Round=1 BestEpoch=  1 Acc=0.2506 F1=0.0191 Precision=0.0119 Recall=0.0476 Training_time=3.4 s 

|2025-01-11 14:25:54| ********************Experiment Results:********************
|2025-01-11 14:25:54| Acc: 0.2506 ± 0.0000
|2025-01-11 14:25:54| F1: 0.0191 ± 0.0000
|2025-01-11 14:25:54| P: 0.0119 ± 0.0000
|2025-01-11 14:25:54| Recall: 0.0476 ± 0.0000
|2025-01-11 14:25:54| train_time: 3.4297 ± 0.0000
|2025-01-11 14:25:54| Skip the efficiency calculation
|2025-01-11 14:25:55| ********************Experiment Success********************
```

