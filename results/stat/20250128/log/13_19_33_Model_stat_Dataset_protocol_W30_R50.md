```python
|2025-01-28 13:19:33| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x10c66ce9f710>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 13:19:33| ********************Experiment Start********************
|2025-01-28 13:25:45| Round=1 BestEpoch= 68 Ac=0.6386 Pr=0.7387 Rc=0.6343 F1=0.6528 Training_time=8.5 s 

|2025-01-28 13:26:03| Round=2 BestEpoch= 53 Ac=0.7376 Pr=0.8305 Rc=0.7569 F1=0.7701 Training_time=6.3 s 

|2025-01-28 13:26:03| ********************Experiment Results:********************
|2025-01-28 13:26:03| AC: 0.6881 ± 0.0495
|2025-01-28 13:26:03| PR: 0.7846 ± 0.0459
|2025-01-28 13:26:03| RC: 0.6956 ± 0.0613
|2025-01-28 13:26:03| F1: 0.7114 ± 0.0587
|2025-01-28 13:26:03| train_time: 7.3947 ± 1.0681
|2025-01-28 13:26:03| Flops: 179072
|2025-01-28 13:26:03| Params: 2736
|2025-01-28 13:26:03| Inference time: 0.04 ms
|2025-01-28 13:26:04| ********************Experiment Success********************
```

