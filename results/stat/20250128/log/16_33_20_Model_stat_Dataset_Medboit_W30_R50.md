```python
|2025-01-28 16:33:20| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xd105d3cf6e0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 16:33:20| ********************Experiment Start********************
|2025-01-28 16:33:21| Ac=0.7329 Pr=0.6903 Rc=0.5913 F1=0.6197 time=34.2 s 
|2025-01-28 16:33:21| Ac=0.7309 Pr=0.6971 Rc=0.6469 F1=0.6618 time=46.2 s 
|2025-01-28 16:33:21| ********************Experiment Results:********************
|2025-01-28 16:33:21| AC: 0.7319 ± 0.0010
|2025-01-28 16:33:21| PR: 0.6937 ± 0.0034
|2025-01-28 16:33:21| RC: 0.6191 ± 0.0278
|2025-01-28 16:33:21| F1: 0.6408 ± 0.0210
|2025-01-28 16:33:21| train_time: 40.2266 ± 5.9775
|2025-01-28 16:33:21| Flops: 165248
|2025-01-28 16:33:21| Params: 2524
|2025-01-28 16:33:21| Inference time: 0.05 ms
|2025-01-28 16:33:21| ********************Experiment Success********************
```

