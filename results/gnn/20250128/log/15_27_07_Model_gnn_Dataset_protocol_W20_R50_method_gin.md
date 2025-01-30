```python
|2025-01-28 15:27:07| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x7f6ce1e3440>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 2, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 2, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-28 15:27:07| ********************Experiment Start********************
|2025-01-28 15:27:08| Ac=0.5474 Pr=0.6115 Rc=0.5617 F1=0.5783 time=3.4 s 
|2025-01-28 15:27:08| Ac=0.5839 Pr=0.6525 Rc=0.5678 F1=0.5935 time=3.6 s 
|2025-01-28 15:27:08| ********************Experiment Results:********************
|2025-01-28 15:27:08| AC: 0.5657 ± 0.0182
|2025-01-28 15:27:08| PR: 0.6320 ± 0.0205
|2025-01-28 15:27:08| RC: 0.5647 ± 0.0031
|2025-01-28 15:27:08| F1: 0.5859 ± 0.0076
|2025-01-28 15:27:08| train_time: 3.4869 ± 0.1085
|2025-01-28 15:27:09| Flops: 4288000
|2025-01-28 15:27:09| Params: 14762
|2025-01-28 15:27:09| Inference time: 0.28 ms
|2025-01-28 15:27:09| ********************Experiment Success********************
```

