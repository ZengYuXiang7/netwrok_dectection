```python
|2025-01-29 20:35:03| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 10, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xef0c2797cb0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 52, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 20:35:03| ********************Experiment Start********************
|2025-01-29 20:35:04| Ac=0.8416 Pr=0.6581 Rc=0.6429 F1=0.6426 time=20.4 s 
|2025-01-29 20:35:04| ********************Experiment Results:********************
|2025-01-29 20:35:04| AC: 0.8416 ± 0.0000
|2025-01-29 20:35:04| PR: 0.6581 ± 0.0000
|2025-01-29 20:35:04| RC: 0.6429 ± 0.0000
|2025-01-29 20:35:04| F1: 0.6426 ± 0.0000
|2025-01-29 20:35:04| train_time: 20.3633 ± 0.0000
|2025-01-29 20:35:05| Flops: 998400
|2025-01-29 20:35:05| Params: 9273
|2025-01-29 20:35:05| Inference time: 1.33 ms
|2025-01-29 20:35:05| ********************Experiment Success********************
```

