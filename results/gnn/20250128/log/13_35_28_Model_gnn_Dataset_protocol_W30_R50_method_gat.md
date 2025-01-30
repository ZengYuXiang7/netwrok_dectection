```python
|2025-01-28 13:35:28| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0x11787040a3c0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-28 13:35:28| ********************Experiment Start********************
|2025-01-28 13:36:04| Round=1 BestEpoch= 75 Ac=0.6485 Pr=0.7434 Rc=0.6989 F1=0.7032 Training_time=15.9 s 

|2025-01-28 13:36:04| ********************Experiment Results:********************
|2025-01-28 13:36:04| AC: 0.6485 ± 0.0000
|2025-01-28 13:36:04| PR: 0.7434 ± 0.0000
|2025-01-28 13:36:04| RC: 0.6989 ± 0.0000
|2025-01-28 13:36:04| F1: 0.7032 ± 0.0000
|2025-01-28 13:36:04| train_time: 15.8866 ± 0.0000
|2025-01-28 13:36:05| Flops: 31200000
|2025-01-28 13:36:05| Params: 33412
|2025-01-28 13:36:05| Inference time: 1.48 ms
|2025-01-28 13:36:05| ********************Experiment Success********************
```

