```python
|2025-01-28 13:34:44| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xe1d588c0bf0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-28 13:34:44| ********************Experiment Start********************
|2025-01-28 13:35:25| Round=1 BestEpoch= 90 Ac=0.6485 Pr=0.7374 Rc=0.6714 F1=0.6744 Training_time=15.8 s 

|2025-01-28 13:35:25| ********************Experiment Results:********************
|2025-01-28 13:35:25| AC: 0.6485 ± 0.0000
|2025-01-28 13:35:25| PR: 0.7374 ± 0.0000
|2025-01-28 13:35:25| RC: 0.6714 ± 0.0000
|2025-01-28 13:35:25| F1: 0.6744 ± 0.0000
|2025-01-28 13:35:25| train_time: 15.7556 ± 0.0000
|2025-01-28 13:35:26| Flops: 2400000
|2025-01-28 13:35:26| Params: 18412
|2025-01-28 13:35:26| Inference time: 1.21 ms
|2025-01-28 13:35:26| ********************Experiment Success********************
```

