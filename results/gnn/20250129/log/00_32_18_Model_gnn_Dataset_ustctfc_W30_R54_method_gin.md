```python
|2025-01-29 00:32:18| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x1374acf903e0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 2, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 54, 'record': True,
     'retrain': False, 'rounds': 2, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 00:32:18| ********************Experiment Start********************
|2025-01-29 00:34:26| Round=1 BestEpoch= 34 Ac=0.6518 Pr=0.5964 Rc=0.5538 F1=0.5463 Training_time=52.5 s 

|2025-01-29 00:38:29| Round=2 BestEpoch= 62 Ac=0.6553 Pr=0.5885 Rc=0.5570 F1=0.5455 Training_time=148.6 s 

|2025-01-29 00:38:29| ********************Experiment Results:********************
|2025-01-29 00:38:29| AC: 0.6536 ± 0.0018
|2025-01-29 00:38:29| PR: 0.5924 ± 0.0040
|2025-01-29 00:38:29| RC: 0.5554 ± 0.0016
|2025-01-29 00:38:29| F1: 0.5459 ± 0.0004
|2025-01-29 00:38:29| train_time: 100.5561 ± 48.0720
|2025-01-29 00:38:39| Flops: 8190720
|2025-01-29 00:38:39| Params: 35606
|2025-01-29 00:38:39| Inference time: 0.25 ms
|2025-01-29 00:38:40| ********************Experiment Success********************
```

