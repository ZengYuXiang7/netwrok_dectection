```python
|2025-01-28 14:46:54| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xea7384d6ed0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 14:46:54| ********************Experiment Start********************
|2025-01-28 14:47:17| Round=1 BestEpoch= 86 Ac=0.5724 Pr=0.5019 Rc=0.4960 F1=0.4838 Training_time=8.8 s 

|2025-01-28 14:47:40| Round=2 BestEpoch= 98 Ac=0.5972 Pr=0.5842 Rc=0.5619 F1=0.5573 Training_time=9.8 s 

|2025-01-28 14:47:40| ********************Experiment Results:********************
|2025-01-28 14:47:40| AC: 0.5848 ± 0.0124
|2025-01-28 14:47:40| PR: 0.5431 ± 0.0411
|2025-01-28 14:47:40| RC: 0.5290 ± 0.0330
|2025-01-28 14:47:40| F1: 0.5206 ± 0.0367
|2025-01-28 14:47:40| train_time: 9.3196 ± 0.4739
|2025-01-28 14:47:40| Flops: 84864000
|2025-01-28 14:47:40| Params: 58027
|2025-01-28 14:47:40| Inference time: 0.07 ms
|2025-01-28 14:47:41| ********************Experiment Success********************
```

