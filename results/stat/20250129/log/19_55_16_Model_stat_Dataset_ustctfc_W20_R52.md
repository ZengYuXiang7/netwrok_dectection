```python
|2025-01-29 19:55:16| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x111924806cc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 19:55:16| ********************Experiment Start********************
|2025-01-29 19:56:47| Round=1 BestEpoch=125 Ac=0.8600 Pr=0.7788 Rc=0.5728 F1=0.6331 Training_time=15.3 s 

|2025-01-29 19:57:13| Round=2 BestEpoch= 86 Ac=0.7900 Pr=0.5699 Rc=0.4691 F1=0.4894 Training_time=10.5 s 

|2025-01-29 19:57:13| ********************Experiment Results:********************
|2025-01-29 19:57:13| AC: 0.8250 ± 0.0350
|2025-01-29 19:57:13| PR: 0.6743 ± 0.1045
|2025-01-29 19:57:13| RC: 0.5210 ± 0.0519
|2025-01-29 19:57:13| F1: 0.5612 ± 0.0718
|2025-01-29 19:57:13| train_time: 12.9107 ± 2.3702
|2025-01-29 19:57:13| Flops: 204032
|2025-01-29 19:57:13| Params: 3119
|2025-01-29 19:57:13| Inference time: 0.04 ms
|2025-01-29 19:57:14| ********************Experiment Success********************
```

