```python
|2025-01-27 18:03:35| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xbbb22e2bb30>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-27 18:03:35| ********************Experiment Start********************
|2025-01-27 18:03:36| Ac=0.0331 Pr=0.0063 Rc=0.0459 F1=0.0048 time=86.0 s 
|2025-01-27 18:03:36| Ac=0.0341 Pr=0.0016 Rc=0.0473 F1=0.0031 time=124.2 s 
|2025-01-27 18:03:36| ********************Experiment Results:********************
|2025-01-27 18:03:36| AC: 0.0336 ± 0.0005
|2025-01-27 18:03:36| PR: 0.0040 ± 0.0023
|2025-01-27 18:03:36| RC: 0.0466 ± 0.0007
|2025-01-27 18:03:36| F1: 0.0040 ± 0.0008
|2025-01-27 18:03:36| train_time: 105.1380 ± 19.1034
|2025-01-27 18:03:36| Flops: 126144000
|2025-01-27 18:03:36| Params: 62521
|2025-01-27 18:03:36| Inference time: 0.09 ms
|2025-01-27 18:03:36| ********************Experiment Success********************
```

