```python
|2025-01-29 21:34:00| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0xc292abd3800>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 21:34:00| ********************Experiment Start********************
|2025-01-29 21:34:49| Round=1 BestEpoch= 95 Ac=0.8641 Pr=0.4836 Rc=0.4492 F1=0.4619 Training_time=25.7 s 

|2025-01-29 21:34:49| ********************Experiment Results:********************
|2025-01-29 21:34:49| AC: 0.8641 ± 0.0000
|2025-01-29 21:34:49| PR: 0.4836 ± 0.0000
|2025-01-29 21:34:49| RC: 0.4492 ± 0.0000
|2025-01-29 21:34:49| F1: 0.4619 ± 0.0000
|2025-01-29 21:34:49| train_time: 25.7062 ± 0.0000
|2025-01-29 21:34:50| Flops: 22830080
|2025-01-29 21:34:50| Params: 35378
|2025-01-29 21:34:50| Inference time: 1.55 ms
|2025-01-29 21:34:50| ********************Experiment Success********************
```

