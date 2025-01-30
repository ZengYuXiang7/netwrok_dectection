```python
|2025-01-30 13:18:12| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x124d5e736cc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-30 13:18:12| ********************Experiment Start********************
|2025-01-30 13:21:25| Round=1 BestEpoch= 55 Ac=0.9829 Pr=0.4357 Rc=0.3585 F1=0.3746 Training_time=36.4 s 

|2025-01-30 13:22:52| Round=2 BestEpoch= 66 Ac=0.9808 Pr=0.4144 Rc=0.4384 F1=0.4112 Training_time=49.2 s 

|2025-01-30 13:24:50| Round=3 BestEpoch=100 Ac=0.9797 Pr=0.3551 Rc=0.3705 F1=0.3569 Training_time=72.9 s 

|2025-01-30 13:26:01| Round=4 BestEpoch= 49 Ac=0.9818 Pr=0.4377 Rc=0.4028 F1=0.4037 Training_time=35.8 s 

|2025-01-30 13:27:23| Round=5 BestEpoch= 58 Ac=0.9797 Pr=0.4836 Rc=0.4193 F1=0.4267 Training_time=43.1 s 

|2025-01-30 13:27:23| ********************Experiment Results:********************
|2025-01-30 13:27:23| AC: 0.9810 ± 0.0012
|2025-01-30 13:27:23| PR: 0.4253 ± 0.0417
|2025-01-30 13:27:23| RC: 0.3979 ± 0.0298
|2025-01-30 13:27:23| F1: 0.3946 ± 0.0253
|2025-01-30 13:27:23| train_time: 47.4778 ± 13.6215
|2025-01-30 13:27:23| Flops: 224000
|2025-01-30 13:27:23| Params: 3425
|2025-01-30 13:27:23| Inference time: 0.04 ms
|2025-01-30 13:27:24| ********************Experiment Success********************
```

