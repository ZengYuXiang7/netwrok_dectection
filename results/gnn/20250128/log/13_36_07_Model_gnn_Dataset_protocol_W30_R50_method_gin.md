```python
|2025-01-28 13:36:07| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x72b2e3a8d10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 2, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 2, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-28 13:36:07| ********************Experiment Start********************
|2025-01-28 13:36:31| Round=1 BestEpoch= 67 Ac=0.5545 Pr=0.6406 Rc=0.5539 F1=0.5836 Training_time=9.1 s 

|2025-01-28 13:36:56| Round=2 BestEpoch= 70 Ac=0.5693 Pr=0.6413 Rc=0.5645 F1=0.5887 Training_time=9.9 s 

|2025-01-28 13:36:56| ********************Experiment Results:********************
|2025-01-28 13:36:56| AC: 0.5619 ± 0.0074
|2025-01-28 13:36:56| PR: 0.6410 ± 0.0004
|2025-01-28 13:36:56| RC: 0.5592 ± 0.0053
|2025-01-28 13:36:56| F1: 0.5861 ± 0.0025
|2025-01-28 13:36:56| train_time: 9.5099 ± 0.3669
|2025-01-28 13:36:56| Flops: 6432000
|2025-01-28 13:36:56| Params: 20762
|2025-01-28 13:36:56| Inference time: 0.24 ms
|2025-01-28 13:36:57| ********************Experiment Success********************
```

