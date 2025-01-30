```python
|2025-01-29 20:02:00| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x136024f13680>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.0025, 'model': graphiot, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 20:02:00| ********************Experiment Start********************
|2025-01-29 20:02:38| Round=1 BestEpoch= 91 Ac=0.8650 Pr=0.7395 Rc=0.7110 F1=0.7162 Training_time=17.2 s 

|2025-01-29 20:02:59| Round=2 BestEpoch= 33 Ac=0.8300 Pr=0.6900 Rc=0.6121 F1=0.6284 Training_time=6.4 s 

|2025-01-29 20:02:59| ********************Experiment Results:********************
|2025-01-29 20:02:59| AC: 0.8475 ± 0.0175
|2025-01-29 20:02:59| PR: 0.7148 ± 0.0248
|2025-01-29 20:02:59| RC: 0.6616 ± 0.0495
|2025-01-29 20:02:59| F1: 0.6723 ± 0.0439
|2025-01-29 20:02:59| train_time: 11.8147 ± 5.3907
|2025-01-29 20:02:59| Flops: 33782528
|2025-01-29 20:02:59| Params: 28513
|2025-01-29 20:02:59| Inference time: 0.83 ms
|2025-01-29 20:03:00| ********************Experiment Success********************
```

