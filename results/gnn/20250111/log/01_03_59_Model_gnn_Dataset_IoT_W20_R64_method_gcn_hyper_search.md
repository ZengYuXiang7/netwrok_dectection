```python
|2025-01-11 01:03:59| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x74b15af22d50>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 6, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 64, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 01:03:59| ********************Experiment Start********************
|2025-01-11 01:44:12| Round=1 BestEpoch=307 Acc=0.8307 F1=0.7549 Precision=0.7697 Recall=0.7438 Training_time=1914.8 s 

|2025-01-11 01:44:12| ********************Experiment Results:********************
|2025-01-11 01:44:12| Acc: 0.8307 ± 0.0000
|2025-01-11 01:44:12| F1: 0.7549 ± 0.0000
|2025-01-11 01:44:12| P: 0.7697 ± 0.0000
|2025-01-11 01:44:12| Recall: 0.7438 ± 0.0000
|2025-01-11 01:44:12| train_time: 1914.8022 ± 0.0000
|2025-01-11 01:44:37| Flops: 2785280
|2025-01-11 01:44:37| Params: 27413
|2025-01-11 01:44:37| Inference time: 1.24 ms
|2025-01-11 01:44:38| ********************Experiment Success********************
```

