```python
|2025-01-29 20:16:21| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x1246d0d2e600>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 20:16:21| ********************Experiment Start********************
|2025-01-29 20:17:36| Round=1 BestEpoch= 60 Ac=0.8571 Pr=0.7510 Rc=0.5674 F1=0.6218 Training_time=6.7 s 

|2025-01-29 20:17:52| Round=2 BestEpoch= 56 Ac=0.8647 Pr=0.6256 Rc=0.6297 F1=0.6176 Training_time=6.1 s 

|2025-01-29 20:17:52| ********************Experiment Results:********************
|2025-01-29 20:17:52| AC: 0.8609 ± 0.0038
|2025-01-29 20:17:52| PR: 0.6883 ± 0.0627
|2025-01-29 20:17:52| RC: 0.5986 ± 0.0311
|2025-01-29 20:17:52| F1: 0.6197 ± 0.0021
|2025-01-29 20:17:52| train_time: 6.3902 ± 0.2784
|2025-01-29 20:17:53| Flops: 204032
|2025-01-29 20:17:53| Params: 3119
|2025-01-29 20:17:53| Inference time: 0.04 ms
|2025-01-29 20:17:53| ********************Experiment Success********************
```

