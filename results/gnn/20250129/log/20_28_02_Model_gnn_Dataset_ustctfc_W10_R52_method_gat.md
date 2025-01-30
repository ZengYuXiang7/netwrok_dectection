```python
|2025-01-29 20:28:02| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 10, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0xa92a67f4980>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 20:28:02| ********************Experiment Start********************
|2025-01-29 20:28:50| Round=1 BestEpoch= 74 Ac=0.8798 Pr=0.7364 Rc=0.7861 F1=0.7439 Training_time=23.2 s 

|2025-01-29 20:28:50| ********************Experiment Results:********************
|2025-01-29 20:28:50| AC: 0.8798 ± 0.0000
|2025-01-29 20:28:50| PR: 0.7364 ± 0.0000
|2025-01-29 20:28:50| RC: 0.7861 ± 0.0000
|2025-01-29 20:28:50| F1: 0.7439 ± 0.0000
|2025-01-29 20:28:50| train_time: 23.2211 ± 0.0000
|2025-01-29 20:28:51| Flops: 11381760
|2025-01-29 20:28:51| Params: 25497
|2025-01-29 20:28:51| Inference time: 1.56 ms
|2025-01-29 20:28:51| ********************Experiment Success********************
```

