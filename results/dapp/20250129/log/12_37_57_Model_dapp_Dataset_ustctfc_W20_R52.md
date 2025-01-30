```python
|2025-01-29 12:37:57| {
     'ablation': 0, 'bs': 150, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x1225478cec00>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': dapp, 'num_classes': 21,
     'optim': AdamW, 'order': 2, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 52, 'record': True, 'retrain': False,
     'rounds': 2, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'try_exp': -1, 'verbose': 10,
}
|2025-01-29 12:37:57| ********************Experiment Start********************
|2025-01-29 12:41:38| Round=1 BestEpoch= 97 Ac=0.4233 Pr=0.2476 Rc=0.3426 F1=0.2625 Training_time=133.0 s 

|2025-01-29 12:43:04| Round=2 BestEpoch= 10 Ac=0.0271 Pr=0.1972 Rc=0.2097 F1=0.1581 Training_time=15.4 s 

|2025-01-29 12:43:04| ********************Experiment Results:********************
|2025-01-29 12:43:04| AC: 0.2252 ± 0.1981
|2025-01-29 12:43:04| PR: 0.2224 ± 0.0252
|2025-01-29 12:43:04| RC: 0.2762 ± 0.0665
|2025-01-29 12:43:04| F1: 0.2103 ± 0.0522
|2025-01-29 12:43:04| train_time: 74.1800 ± 58.8033
|2025-01-29 12:43:17| Flops: 75504000
|2025-01-29 12:43:17| Params: 28360
|2025-01-29 12:43:17| Inference time: 0.72 ms
|2025-01-29 12:43:18| ********************Experiment Success********************
```

