```python
|2025-01-29 20:19:12| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 10, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xa1802a6fc20>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 20:19:12| ********************Experiment Start********************
|2025-01-29 20:20:55| Round=1 BestEpoch=110 Ac=0.9062 Pr=0.8000 Rc=0.8153 F1=0.7961 Training_time=20.2 s 

|2025-01-29 20:21:23| Round=2 BestEpoch= 42 Ac=0.8680 Pr=0.7084 Rc=0.6656 F1=0.6823 Training_time=7.7 s 

|2025-01-29 20:21:23| ********************Experiment Results:********************
|2025-01-29 20:21:23| AC: 0.8871 ± 0.0191
|2025-01-29 20:21:23| PR: 0.7542 ± 0.0458
|2025-01-29 20:21:23| RC: 0.7405 ± 0.0748
|2025-01-29 20:21:23| F1: 0.7392 ± 0.0569
|2025-01-29 20:21:23| train_time: 13.9602 ± 6.2562
|2025-01-29 20:21:23| Flops: 247010816
|2025-01-29 20:21:23| Params: 215297
|2025-01-29 20:21:23| Inference time: 0.55 ms
|2025-01-29 20:21:23| ********************Experiment Success********************
```

