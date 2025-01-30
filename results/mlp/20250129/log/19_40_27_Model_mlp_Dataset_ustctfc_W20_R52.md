```python
|2025-01-29 19:40:27| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xb8bf2370d10>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 19:40:27| ********************Experiment Start********************
|2025-01-29 19:40:54| Round=1 BestEpoch= 12 Ac=0.9940 Pr=0.7450 Rc=0.6336 F1=0.6637 Training_time=6.0 s 

|2025-01-29 19:41:27| Round=2 BestEpoch= 22 Ac=0.9956 Pr=0.7994 Rc=0.6986 F1=0.7392 Training_time=10.7 s 

|2025-01-29 19:41:27| ********************Experiment Results:********************
|2025-01-29 19:41:27| AC: 0.9948 ± 0.0008
|2025-01-29 19:41:27| PR: 0.7722 ± 0.0272
|2025-01-29 19:41:27| RC: 0.6661 ± 0.0325
|2025-01-29 19:41:27| F1: 0.7015 ± 0.0378
|2025-01-29 19:41:27| train_time: 8.3377 ± 2.3366
|2025-01-29 19:41:27| Flops: 604160
|2025-01-29 19:41:27| Params: 4606
|2025-01-29 19:41:27| Inference time: 0.06 ms
|2025-01-29 19:41:28| ********************Experiment Success********************
```

