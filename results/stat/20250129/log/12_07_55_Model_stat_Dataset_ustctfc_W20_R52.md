```python
|2025-01-29 12:07:55| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x6033aaa6600>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 12:07:55| ********************Experiment Start********************
|2025-01-29 12:10:52| Round=1 BestEpoch= 34 Ac=0.6094 Pr=0.3673 Rc=0.3398 F1=0.3384 Training_time=22.7 s 

|2025-01-29 12:11:50| Round=2 BestEpoch= 39 Ac=0.6061 Pr=0.3138 Rc=0.2920 F1=0.2913 Training_time=25.9 s 

|2025-01-29 12:11:50| ********************Experiment Results:********************
|2025-01-29 12:11:50| AC: 0.6077 ± 0.0016
|2025-01-29 12:11:50| PR: 0.3405 ± 0.0268
|2025-01-29 12:11:50| RC: 0.3159 ± 0.0239
|2025-01-29 12:11:50| F1: 0.3149 ± 0.0235
|2025-01-29 12:11:50| train_time: 24.2929 ± 1.6231
|2025-01-29 12:11:50| Flops: 214784
|2025-01-29 12:11:50| Params: 3284
|2025-01-29 12:11:50| Inference time: 0.04 ms
|2025-01-29 12:11:51| ********************Experiment Success********************
```

