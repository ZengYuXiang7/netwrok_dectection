```python
|2025-01-27 19:21:00| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x128ca00a0e00>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-27 19:21:00| ********************Experiment Start********************
|2025-01-27 19:25:44| Round=1 BestEpoch=349 Ac=0.7873 Pr=0.7059 Rc=0.6709 F1=0.6822 Training_time=209.0 s 

|2025-01-27 19:29:37| Round=2 BestEpoch=281 Ac=0.7805 Pr=0.6882 Rc=0.6643 F1=0.6732 Training_time=167.5 s 

|2025-01-27 19:29:37| ********************Experiment Results:********************
|2025-01-27 19:29:37| AC: 0.7839 ± 0.0034
|2025-01-27 19:29:37| PR: 0.6971 ± 0.0089
|2025-01-27 19:29:37| RC: 0.6676 ± 0.0033
|2025-01-27 19:29:37| F1: 0.6777 ± 0.0045
|2025-01-27 19:29:37| train_time: 188.2432 ± 20.7797
|2025-01-27 19:29:37| Flops: 708352
|2025-01-27 19:29:37| Params: 5413
|2025-01-27 19:29:37| Inference time: 0.06 ms
|2025-01-27 19:29:38| ********************Experiment Success********************
```

