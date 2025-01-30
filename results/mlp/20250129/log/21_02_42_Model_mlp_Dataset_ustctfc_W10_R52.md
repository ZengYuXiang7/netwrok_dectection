```python
|2025-01-29 21:02:42| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 10, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xcdd7af58b90>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 21:02:42| ********************Experiment Start********************
|2025-01-29 21:03:12| Round=1 BestEpoch= 42 Ac=0.9793 Pr=0.6488 Rc=0.5986 F1=0.6102 Training_time=12.9 s 

|2025-01-29 21:03:28| Round=2 BestEpoch=  7 Ac=0.9787 Pr=0.5814 Rc=0.5435 F1=0.5543 Training_time=2.1 s 

|2025-01-29 21:03:28| ********************Experiment Results:********************
|2025-01-29 21:03:28| AC: 0.9790 ± 0.0003
|2025-01-29 21:03:28| PR: 0.6151 ± 0.0337
|2025-01-29 21:03:28| RC: 0.5710 ± 0.0275
|2025-01-29 21:03:28| F1: 0.5822 ± 0.0279
|2025-01-29 21:03:28| train_time: 7.5243 ± 5.3834
|2025-01-29 21:03:28| Flops: 602112
|2025-01-29 21:03:28| Params: 4581
|2025-01-29 21:03:28| Inference time: 0.06 ms
|2025-01-29 21:03:28| ********************Experiment Success********************
```

