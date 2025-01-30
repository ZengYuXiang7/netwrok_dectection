```python
|2025-01-28 13:33:05| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x136e96b8bc20>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 13:33:05| ********************Experiment Start********************
|2025-01-28 13:33:56| Round=1 BestEpoch=229 Ac=0.5594 Pr=0.6176 Rc=0.5105 F1=0.5384 Training_time=24.7 s 

|2025-01-28 13:34:40| Round=2 BestEpoch=196 Ac=0.5990 Pr=0.6973 Rc=0.6058 F1=0.5947 Training_time=21.0 s 

|2025-01-28 13:34:40| ********************Experiment Results:********************
|2025-01-28 13:34:40| AC: 0.5792 ± 0.0198
|2025-01-28 13:34:40| PR: 0.6575 ± 0.0399
|2025-01-28 13:34:40| RC: 0.5582 ± 0.0477
|2025-01-28 13:34:40| F1: 0.5665 ± 0.0282
|2025-01-28 13:34:40| train_time: 22.8517 ± 1.8952
|2025-01-28 13:34:41| Flops: 31187200
|2025-01-28 13:34:41| Params: 8562
|2025-01-28 13:34:41| Inference time: 0.09 ms
|2025-01-28 13:34:41| ********************Experiment Success********************
```

