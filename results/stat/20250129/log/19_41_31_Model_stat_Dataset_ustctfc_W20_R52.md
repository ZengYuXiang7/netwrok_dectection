```python
|2025-01-29 19:41:31| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xcc1fd24ee40>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 19:41:31| ********************Experiment Start********************
|2025-01-29 19:46:25| Round=1 BestEpoch=170 Ac=0.9941 Pr=0.6241 Rc=0.6043 F1=0.6115 Training_time=124.5 s 

|2025-01-29 19:48:25| Round=2 BestEpoch=100 Ac=0.9933 Pr=0.7189 Rc=0.6155 F1=0.6292 Training_time=74.5 s 

|2025-01-29 19:48:25| ********************Experiment Results:********************
|2025-01-29 19:48:25| AC: 0.9937 ± 0.0004
|2025-01-29 19:48:25| PR: 0.6715 ± 0.0474
|2025-01-29 19:48:25| RC: 0.6099 ± 0.0056
|2025-01-29 19:48:25| F1: 0.6203 ± 0.0088
|2025-01-29 19:48:25| train_time: 99.4737 ± 24.9800
|2025-01-29 19:48:25| Flops: 178944
|2025-01-29 19:48:25| Params: 2734
|2025-01-29 19:48:25| Inference time: 0.04 ms
|2025-01-29 19:48:25| ********************Experiment Success********************
```

