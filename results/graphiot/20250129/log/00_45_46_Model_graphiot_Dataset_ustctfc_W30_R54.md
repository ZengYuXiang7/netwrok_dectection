```python
|2025-01-29 00:45:46| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x6d13fce4620>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.0025, 'model': graphiot, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 54, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 00:45:46| ********************Experiment Start********************
|2025-01-29 00:49:57| Round=1 BestEpoch= 45 Ac=0.6058 Pr=0.5249 Rc=0.5295 F1=0.5089 Training_time=116.1 s 

|2025-01-29 00:54:33| Round=2 BestEpoch= 46 Ac=0.3687 Pr=0.3537 Rc=0.4593 F1=0.3500 Training_time=147.5 s 

|2025-01-29 00:54:33| ********************Experiment Results:********************
|2025-01-29 00:54:33| AC: 0.4873 ± 0.1185
|2025-01-29 00:54:33| PR: 0.4393 ± 0.0856
|2025-01-29 00:54:33| RC: 0.4944 ± 0.0351
|2025-01-29 00:54:33| F1: 0.4294 ± 0.0795
|2025-01-29 00:54:33| train_time: 131.8195 ± 15.6918
|2025-01-29 00:54:44| Flops: 54432000
|2025-01-29 00:54:44| Params: 31070
|2025-01-29 00:54:44| Inference time: 0.92 ms
|2025-01-29 00:54:45| ********************Experiment Success********************
```

