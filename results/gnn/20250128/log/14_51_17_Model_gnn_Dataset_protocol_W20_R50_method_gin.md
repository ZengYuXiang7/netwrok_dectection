```python
|2025-01-28 14:51:17| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x8a3081488f0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 2, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 2, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-28 14:51:17| ********************Experiment Start********************
|2025-01-28 14:51:18| Ac=0.5866 Pr=0.5062 Rc=0.5088 F1=0.4979 time=11.9 s 
|2025-01-28 14:51:18| Ac=0.5477 Pr=0.4961 Rc=0.4418 F1=0.4491 time=4.2 s 
|2025-01-28 14:51:18| ********************Experiment Results:********************
|2025-01-28 14:51:18| AC: 0.5671 ± 0.0194
|2025-01-28 14:51:18| PR: 0.5011 ± 0.0050
|2025-01-28 14:51:18| RC: 0.4753 ± 0.0335
|2025-01-28 14:51:18| F1: 0.4735 ± 0.0244
|2025-01-28 14:51:18| train_time: 8.0549 ± 3.8239
|2025-01-28 14:51:19| Flops: 5248000
|2025-01-28 14:51:19| Params: 29777
|2025-01-28 14:51:19| Inference time: 0.27 ms
|2025-01-28 14:51:19| ********************Experiment Success********************
```

