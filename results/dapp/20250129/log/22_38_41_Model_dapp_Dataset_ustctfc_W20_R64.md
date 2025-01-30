```python
|2025-01-29 22:38:41| {
     'ablation': 0, 'bs': 150, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xd2bc0d0f950>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': dapp, 'num_classes': 21,
     'optim': AdamW, 'order': 2, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 64, 'record': True, 'retrain': False,
     'rounds': 5, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'try_exp': -1, 'verbose': 10,
}
|2025-01-29 22:38:41| ********************Experiment Start********************
|2025-01-29 22:39:12| Round=1 BestEpoch=100 Ac=0.8544 Pr=0.5136 Rc=0.4455 F1=0.4567 Training_time=13.8 s 

|2025-01-29 22:39:30| Round=2 BestEpoch= 44 Ac=0.8058 Pr=0.3607 Rc=0.3635 F1=0.3613 Training_time=6.3 s 

|2025-01-29 22:40:12| Round=3 BestEpoch=136 Ac=0.8608 Pr=0.4933 Rc=0.4478 F1=0.4441 Training_time=20.0 s 

|2025-01-29 22:41:04| Round=4 BestEpoch=177 Ac=0.8738 Pr=0.4728 Rc=0.4763 F1=0.4718 Training_time=26.1 s 

|2025-01-29 22:41:23| Round=5 BestEpoch= 43 Ac=0.8188 Pr=0.3915 Rc=0.4045 F1=0.3945 Training_time=6.4 s 

|2025-01-29 22:41:23| ********************Experiment Results:********************
|2025-01-29 22:41:23| AC: 0.8427 ± 0.0259
|2025-01-29 22:41:23| PR: 0.4464 ± 0.0596
|2025-01-29 22:41:23| RC: 0.4275 ± 0.0394
|2025-01-29 22:41:23| F1: 0.4257 ± 0.0413
|2025-01-29 22:41:23| train_time: 14.5269 ± 7.7209
|2025-01-29 22:41:23| Flops: 113606400
|2025-01-29 22:41:23| Params: 41426
|2025-01-29 22:41:23| Inference time: 0.66 ms
|2025-01-29 22:41:25| ********************Experiment Success********************
```

