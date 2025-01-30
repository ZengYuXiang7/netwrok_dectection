```python
|2025-01-28 14:16:50| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x818b40368a0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-28 14:16:50| ********************Experiment Start********************
|2025-01-28 14:17:35| Round=1 BestEpoch= 95 Ac=0.5093 Pr=0.4692 Rc=0.4518 F1=0.4478 Training_time=18.0 s 

|2025-01-28 14:17:35| ********************Experiment Results:********************
|2025-01-28 14:17:35| AC: 0.5093 ± 0.0000
|2025-01-28 14:17:35| PR: 0.4692 ± 0.0000
|2025-01-28 14:17:35| RC: 0.4518 ± 0.0000
|2025-01-28 14:17:35| F1: 0.4478 ± 0.0000
|2025-01-28 14:17:35| train_time: 18.0161 ± 0.0000
|2025-01-28 14:17:36| Flops: 3840000
|2025-01-28 14:17:36| Params: 40927
|2025-01-28 14:17:36| Inference time: 1.30 ms
|2025-01-28 14:17:36| ********************Experiment Success********************
```

