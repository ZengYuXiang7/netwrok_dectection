```python
|2025-01-28 14:01:52| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x567170af290>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 14:01:52| ********************Experiment Start********************
|2025-01-28 14:08:04| Round=1 BestEpoch= 57 Ac=0.5421 Pr=0.3882 Rc=0.3568 F1=0.3502 Training_time=7.3 s 

|2025-01-28 14:08:21| Round=2 BestEpoch= 47 Ac=0.5607 Pr=0.4625 Rc=0.3998 F1=0.3951 Training_time=5.9 s 

|2025-01-28 14:08:21| ********************Experiment Results:********************
|2025-01-28 14:08:21| AC: 0.5514 ± 0.0093
|2025-01-28 14:08:21| PR: 0.4253 ± 0.0371
|2025-01-28 14:08:21| RC: 0.3783 ± 0.0215
|2025-01-28 14:08:21| F1: 0.3726 ± 0.0225
|2025-01-28 14:08:21| train_time: 6.5984 ± 0.6908
|2025-01-28 14:08:22| Flops: 230912
|2025-01-28 14:08:22| Params: 3531
|2025-01-28 14:08:22| Inference time: 0.04 ms
|2025-01-28 14:08:22| ********************Experiment Success********************
```

