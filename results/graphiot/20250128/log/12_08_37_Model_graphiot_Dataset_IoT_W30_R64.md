```python
|2025-01-28 12:08:37| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xcba8f0711c0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.0025, 'model': graphiot, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 12:08:37| ********************Experiment Start********************
|2025-01-28 12:21:39| Round=1 BestEpoch=151 Ac=0.8911 Pr=0.8530 Rc=0.8087 F1=0.8182 Training_time=570.2 s 

|2025-01-28 12:42:36| Round=2 BestEpoch=242 Ac=0.9057 Pr=0.8557 Rc=0.8473 F1=0.8462 Training_time=983.0 s 

|2025-01-28 12:42:36| ********************Experiment Results:********************
|2025-01-28 12:42:36| AC: 0.8984 ± 0.0073
|2025-01-28 12:42:36| PR: 0.8544 ± 0.0014
|2025-01-28 12:42:36| RC: 0.8280 ± 0.0193
|2025-01-28 12:42:36| F1: 0.8322 ± 0.0140
|2025-01-28 12:42:36| train_time: 776.5717 ± 206.4070
|2025-01-28 12:42:51| Flops: 75583488
|2025-01-28 12:42:51| Params: 42773
|2025-01-28 12:42:51| Inference time: 0.90 ms
|2025-01-28 12:42:52| ********************Experiment Success********************
```

