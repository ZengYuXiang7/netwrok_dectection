```python
|2025-01-29 20:38:49| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xe2aaa477c20>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 20:38:49| ********************Experiment Start********************
|2025-01-29 20:38:50| Ac=0.8150 Pr=0.6560 Rc=0.5745 F1=0.6024 time=4.1 s 
|2025-01-29 20:38:50| Ac=0.8250 Pr=0.7267 Rc=0.5197 F1=0.5769 time=1.3 s 
|2025-01-29 20:38:50| ********************Experiment Results:********************
|2025-01-29 20:38:50| AC: 0.8200 ± 0.0050
|2025-01-29 20:38:50| PR: 0.6914 ± 0.0354
|2025-01-29 20:38:50| RC: 0.5471 ± 0.0274
|2025-01-29 20:38:50| F1: 0.5896 ± 0.0127
|2025-01-29 20:38:50| train_time: 2.6940 ± 1.3732
|2025-01-29 20:38:50| Flops: 654336
|2025-01-29 20:38:50| Params: 4991
|2025-01-29 20:38:50| Inference time: 0.07 ms
|2025-01-29 20:38:50| ********************Experiment Success********************
```

