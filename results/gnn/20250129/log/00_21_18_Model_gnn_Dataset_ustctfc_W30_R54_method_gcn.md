```python
|2025-01-29 00:21:18| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xf91a3d94b30>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 54, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 00:21:18| ********************Experiment Start********************
|2025-01-29 00:26:14| Round=1 BestEpoch= 23 Ac=0.6614 Pr=0.5932 Rc=0.6331 F1=0.6013 Training_time=58.6 s 

|2025-01-29 00:26:14| ********************Experiment Results:********************
|2025-01-29 00:26:14| AC: 0.6614 ± 0.0000
|2025-01-29 00:26:14| PR: 0.5932 ± 0.0000
|2025-01-29 00:26:14| RC: 0.6331 ± 0.0000
|2025-01-29 00:26:14| F1: 0.6013 ± 0.0000
|2025-01-29 00:26:14| train_time: 58.6338 ± 0.0000
|2025-01-29 00:26:24| Flops: 3421440
|2025-01-29 00:26:24| Params: 32852
|2025-01-29 00:26:24| Inference time: 1.30 ms
|2025-01-29 00:26:25| ********************Experiment Success********************
```

