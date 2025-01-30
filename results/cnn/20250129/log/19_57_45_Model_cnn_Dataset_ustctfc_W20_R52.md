```python
|2025-01-29 19:57:45| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x14fefe0bb800>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 19:57:45| ********************Experiment Start********************
|2025-01-29 19:58:21| Round=1 BestEpoch=132 Ac=0.8050 Pr=0.4229 Rc=0.4043 F1=0.4085 Training_time=16.0 s 

|2025-01-29 19:58:58| Round=2 BestEpoch=138 Ac=0.8000 Pr=0.6864 Rc=0.5076 F1=0.5552 Training_time=16.6 s 

|2025-01-29 19:58:58| ********************Experiment Results:********************
|2025-01-29 19:58:58| AC: 0.8025 ± 0.0025
|2025-01-29 19:58:58| PR: 0.5546 ± 0.1318
|2025-01-29 19:58:58| RC: 0.4560 ± 0.0516
|2025-01-29 19:58:58| F1: 0.4818 ± 0.0734
|2025-01-29 19:58:58| train_time: 16.2951 ± 0.2841
|2025-01-29 19:58:58| Flops: 22483968
|2025-01-29 19:58:58| Params: 9481
|2025-01-29 19:58:58| Inference time: 0.08 ms
|2025-01-29 19:58:59| ********************Experiment Success********************
```

