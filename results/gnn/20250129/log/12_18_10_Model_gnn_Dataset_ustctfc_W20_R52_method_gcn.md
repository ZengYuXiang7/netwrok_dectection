```python
|2025-01-29 12:18:10| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x12f240172570>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 52, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 12:18:10| ********************Experiment Start********************
|2025-01-29 12:22:39| Round=1 BestEpoch= 20 Ac=0.6069 Pr=0.4866 Rc=0.4711 F1=0.4646 Training_time=52.9 s 

|2025-01-29 12:22:39| ********************Experiment Results:********************
|2025-01-29 12:22:39| AC: 0.6069 ± 0.0000
|2025-01-29 12:22:39| PR: 0.4866 ± 0.0000
|2025-01-29 12:22:39| RC: 0.4711 ± 0.0000
|2025-01-29 12:22:39| F1: 0.4646 ± 0.0000
|2025-01-29 12:22:39| train_time: 52.9142 ± 0.0000
|2025-01-29 12:22:50| Flops: 2196480
|2025-01-29 12:22:50| Params: 21236
|2025-01-29 12:22:50| Inference time: 1.33 ms
|2025-01-29 12:22:51| ********************Experiment Success********************
```

