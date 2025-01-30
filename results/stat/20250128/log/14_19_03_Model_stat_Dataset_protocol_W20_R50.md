```python
|2025-01-28 14:19:03| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x101ab9c830b0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 14:19:03| ********************Experiment Start********************
|2025-01-28 14:25:25| Round=1 BestEpoch= 90 Ac=0.2175 Pr=0.0723 Rc=0.1068 F1=0.0801 Training_time=12.8 s 

|2025-01-28 14:25:55| Round=2 BestEpoch= 89 Ac=0.2571 Pr=0.0761 Rc=0.1103 F1=0.0842 Training_time=12.5 s 

|2025-01-28 14:25:55| ********************Experiment Results:********************
|2025-01-28 14:25:55| AC: 0.2373 ± 0.0198
|2025-01-28 14:25:55| PR: 0.0742 ± 0.0019
|2025-01-28 14:25:55| RC: 0.1086 ± 0.0018
|2025-01-28 14:25:55| F1: 0.0821 ± 0.0021
|2025-01-28 14:25:55| train_time: 12.6907 ± 0.1530
|2025-01-28 14:25:55| Flops: 621440
|2025-01-28 14:25:55| Params: 9520
|2025-01-28 14:25:55| Inference time: 0.04 ms
|2025-01-28 14:25:56| ********************Experiment Success********************
```

