```python
|2025-01-28 15:26:14| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0xbf4b08aacc0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-28 15:26:14| ********************Experiment Start********************
|2025-01-28 15:26:29| Round=1 BestEpoch=  7 Ac=0.6569 Pr=0.6711 Rc=0.6094 F1=0.6292 Training_time=2.0 s 

|2025-01-28 15:26:29| ********************Experiment Results:********************
|2025-01-28 15:26:29| AC: 0.6569 ± 0.0000
|2025-01-28 15:26:29| PR: 0.6711 ± 0.0000
|2025-01-28 15:26:29| RC: 0.6094 ± 0.0000
|2025-01-28 15:26:29| F1: 0.6292 ± 0.0000
|2025-01-28 15:26:29| train_time: 1.9924 ± 0.0000
|2025-01-28 15:26:30| Flops: 20800000
|2025-01-28 15:26:30| Params: 27412
|2025-01-28 15:26:30| Inference time: 1.56 ms
|2025-01-28 15:26:30| ********************Experiment Success********************
```

