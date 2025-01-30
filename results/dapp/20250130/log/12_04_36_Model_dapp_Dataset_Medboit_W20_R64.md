```python
|2025-01-30 12:04:36| {
     'ablation': 0, 'bs': 150, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x6f56ccb8050>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': dapp, 'num_classes': 21,
     'optim': AdamW, 'order': 2, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 64, 'record': True, 'retrain': False,
     'rounds': 5, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'try_exp': -1, 'verbose': 10,
}
|2025-01-30 12:04:36| ********************Experiment Start********************
|2025-01-30 12:05:33| Round=1 BestEpoch=126 Ac=0.8062 Pr=0.6668 Rc=0.5488 F1=0.5871 Training_time=30.7 s 

|2025-01-30 12:06:06| Round=2 BestEpoch= 49 Ac=0.5779 Pr=0.0963 Rc=0.1667 F1=0.1221 Training_time=13.1 s 

|2025-01-30 12:06:41| Round=3 BestEpoch= 54 Ac=0.6266 Pr=0.2839 Rc=0.2732 F1=0.2638 Training_time=14.5 s 

|2025-01-30 12:07:12| Round=4 BestEpoch= 46 Ac=0.8478 Pr=0.4467 Rc=0.4327 F1=0.4347 Training_time=12.4 s 

|2025-01-30 12:07:48| Round=5 BestEpoch= 55 Ac=0.7360 Pr=0.5704 Rc=0.5378 F1=0.5320 Training_time=14.9 s 

|2025-01-30 12:07:48| ********************Experiment Results:********************
|2025-01-30 12:07:48| AC: 0.7189 ± 0.1029
|2025-01-30 12:07:48| PR: 0.4128 ± 0.2036
|2025-01-30 12:07:48| RC: 0.3918 ± 0.1499
|2025-01-30 12:07:48| F1: 0.3879 ± 0.1724
|2025-01-30 12:07:48| train_time: 17.1323 ± 6.8675
|2025-01-30 12:07:49| Flops: 113260800
|2025-01-30 12:07:49| Params: 39110
|2025-01-30 12:07:49| Inference time: 0.65 ms
|2025-01-30 12:07:51| ********************Experiment Success********************
```

