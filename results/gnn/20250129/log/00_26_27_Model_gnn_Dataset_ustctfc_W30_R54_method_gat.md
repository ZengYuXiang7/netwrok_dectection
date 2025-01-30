```python
|2025-01-29 00:26:27| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0xa1b54f9b350>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 54,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 00:26:27| ********************Experiment Start********************
|2025-01-29 00:32:04| Round=1 BestEpoch= 49 Ac=0.6559 Pr=0.6092 Rc=0.6163 F1=0.5982 Training_time=188.6 s 

|2025-01-29 00:32:04| ********************Experiment Results:********************
|2025-01-29 00:32:04| AC: 0.6559 ± 0.0000
|2025-01-29 00:32:04| PR: 0.6092 ± 0.0000
|2025-01-29 00:32:04| RC: 0.6163 ± 0.0000
|2025-01-29 00:32:04| F1: 0.5982 ± 0.0000
|2025-01-29 00:32:04| train_time: 188.5864 ± 0.0000
|2025-01-29 00:32:15| Flops: 37013760
|2025-01-29 00:32:15| Params: 50348
|2025-01-29 00:32:15| Inference time: 1.64 ms
|2025-01-29 00:32:16| ********************Experiment Success********************
```

