```python
|2025-01-29 00:12:43| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x100339bb3ad0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 54, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 00:12:43| ********************Experiment Start********************
|2025-01-29 00:13:30| Round=1 BestEpoch= 29 Ac=0.6428 Pr=0.4989 Rc=0.4325 F1=0.4453 Training_time=18.8 s 

|2025-01-29 00:14:41| Round=2 BestEpoch= 59 Ac=0.6449 Pr=0.5912 Rc=0.5369 F1=0.5325 Training_time=38.0 s 

|2025-01-29 00:14:41| ********************Experiment Results:********************
|2025-01-29 00:14:41| AC: 0.6438 ± 0.0011
|2025-01-29 00:14:41| PR: 0.5451 ± 0.0461
|2025-01-29 00:14:41| RC: 0.4847 ± 0.0522
|2025-01-29 00:14:41| F1: 0.4889 ± 0.0436
|2025-01-29 00:14:41| train_time: 28.3588 ± 9.5927
|2025-01-29 00:14:41| Flops: 222848
|2025-01-29 00:14:41| Params: 3408
|2025-01-29 00:14:41| Inference time: 0.04 ms
|2025-01-29 00:14:42| ********************Experiment Success********************
```

