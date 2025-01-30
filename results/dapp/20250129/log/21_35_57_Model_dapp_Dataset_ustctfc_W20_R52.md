```python
|2025-01-29 21:35:57| {
     'ablation': 0, 'bs': 150, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x83126b6b4a0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': dapp, 'num_classes': 21,
     'optim': AdamW, 'order': 2, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 52, 'record': True, 'retrain': False,
     'rounds': 2, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'try_exp': -1, 'verbose': 10,
}
|2025-01-29 21:35:57| ********************Experiment Start********************
|2025-01-29 21:36:14| Round=1 BestEpoch= 32 Ac=0.5987 Pr=0.3263 Rc=0.3017 F1=0.2720 Training_time=4.7 s 

|2025-01-29 21:36:50| Round=2 BestEpoch=102 Ac=0.8317 Pr=0.4051 Rc=0.4153 F1=0.4088 Training_time=16.0 s 

|2025-01-29 21:36:50| ********************Experiment Results:********************
|2025-01-29 21:36:50| AC: 0.7152 ± 0.1165
|2025-01-29 21:36:50| PR: 0.3657 ± 0.0394
|2025-01-29 21:36:50| RC: 0.3585 ± 0.0568
|2025-01-29 21:36:50| F1: 0.3404 ± 0.0684
|2025-01-29 21:36:50| train_time: 10.3669 ± 5.6313
|2025-01-29 21:36:51| Flops: 75457200
|2025-01-29 21:36:51| Params: 28046
|2025-01-29 21:36:51| Inference time: 0.67 ms
|2025-01-29 21:36:51| ********************Experiment Success********************
```

