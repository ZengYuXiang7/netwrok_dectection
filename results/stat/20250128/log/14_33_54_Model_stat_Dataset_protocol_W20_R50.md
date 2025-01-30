```python
|2025-01-28 14:33:54| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x11ea8727ae10>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 14:33:54| ********************Experiment Start********************
|2025-01-28 14:39:57| Round=1 BestEpoch= 41 Ac=0.4594 Pr=0.2448 Rc=0.2733 F1=0.2495 Training_time=5.2 s 

|2025-01-28 14:40:16| Round=2 BestEpoch= 52 Ac=0.4947 Pr=0.3676 Rc=0.3313 F1=0.3110 Training_time=6.5 s 

|2025-01-28 14:40:16| ********************Experiment Results:********************
|2025-01-28 14:40:16| AC: 0.4770 ± 0.0177
|2025-01-28 14:40:16| PR: 0.3062 ± 0.0614
|2025-01-28 14:40:16| RC: 0.3023 ± 0.0290
|2025-01-28 14:40:16| F1: 0.2803 ± 0.0307
|2025-01-28 14:40:16| train_time: 5.8260 ± 0.6344
|2025-01-28 14:40:16| Flops: 230912
|2025-01-28 14:40:16| Params: 3531
|2025-01-28 14:40:16| Inference time: 0.04 ms
|2025-01-28 14:40:16| ********************Experiment Success********************
```

