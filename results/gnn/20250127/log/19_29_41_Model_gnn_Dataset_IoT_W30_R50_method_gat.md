```python
|2025-01-27 19:29:41| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0x14fbab2cb260>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-27 19:29:41| ********************Experiment Start********************
|2025-01-27 19:29:53| Ac=0.8678 Pr=0.8009 Rc=0.7914 F1=0.7946 time=817.8 s 
|2025-01-27 19:29:53| ********************Experiment Results:********************
|2025-01-27 19:29:53| AC: 0.8678 ± 0.0000
|2025-01-27 19:29:53| PR: 0.8009 ± 0.0000
|2025-01-27 19:29:53| RC: 0.7914 ± 0.0000
|2025-01-27 19:29:53| F1: 0.7946 ± 0.0000
|2025-01-27 19:29:53| train_time: 817.8018 ± 0.0000
|2025-01-27 19:30:09| Flops: 32064000
|2025-01-27 19:30:09| Params: 46921
|2025-01-27 19:30:09| Inference time: 2.44 ms
|2025-01-27 19:30:09| ********************Experiment Success********************
```

