```python
|2025-01-29 21:29:25| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xdb0a537d6d0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 21:29:25| ********************Experiment Start********************
|2025-01-29 21:30:00| Round=1 BestEpoch=155 Ac=0.8803 Pr=0.4585 Rc=0.4539 F1=0.4546 Training_time=16.0 s 

|2025-01-29 21:30:29| Round=2 BestEpoch=127 Ac=0.8803 Pr=0.5366 Rc=0.4950 F1=0.4970 Training_time=13.1 s 

|2025-01-29 21:30:29| ********************Experiment Results:********************
|2025-01-29 21:30:29| AC: 0.8803 ± 0.0000
|2025-01-29 21:30:29| PR: 0.4976 ± 0.0390
|2025-01-29 21:30:29| RC: 0.4744 ± 0.0206
|2025-01-29 21:30:29| F1: 0.4758 ± 0.0212
|2025-01-29 21:30:29| train_time: 14.5454 ± 1.4944
|2025-01-29 21:30:30| Flops: 90255360
|2025-01-29 21:30:30| Params: 52226
|2025-01-29 21:30:30| Inference time: 0.07 ms
|2025-01-29 21:30:30| ********************Experiment Success********************
```

