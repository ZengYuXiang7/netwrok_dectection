```python
|2025-01-29 20:17:56| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x9db3e4a6c90>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 20:17:56| ********************Experiment Start********************
|2025-01-29 20:18:21| Round=1 BestEpoch= 99 Ac=0.8120 Pr=0.5526 Rc=0.5234 F1=0.5149 Training_time=10.4 s 

|2025-01-29 20:18:42| Round=2 BestEpoch= 80 Ac=0.7669 Pr=0.5234 Rc=0.4579 F1=0.4648 Training_time=8.3 s 

|2025-01-29 20:18:42| ********************Experiment Results:********************
|2025-01-29 20:18:42| AC: 0.7895 ± 0.0226
|2025-01-29 20:18:42| PR: 0.5380 ± 0.0146
|2025-01-29 20:18:42| RC: 0.4907 ± 0.0328
|2025-01-29 20:18:42| F1: 0.4898 ± 0.0251
|2025-01-29 20:18:42| train_time: 9.3573 ± 1.0540
|2025-01-29 20:18:42| Flops: 135183360
|2025-01-29 20:18:42| Params: 60025
|2025-01-29 20:18:42| Inference time: 0.07 ms
|2025-01-29 20:18:43| ********************Experiment Success********************
```

