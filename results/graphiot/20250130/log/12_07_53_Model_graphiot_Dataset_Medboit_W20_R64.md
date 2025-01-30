```python
|2025-01-30 12:07:53| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x96405850380>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.0025, 'model': graphiot, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-30 12:07:53| ********************Experiment Start********************
|2025-01-30 12:08:35| Round=1 BestEpoch= 45 Ac=0.8228 Pr=0.6958 Rc=0.6037 F1=0.5727 Training_time=18.9 s 

|2025-01-30 12:09:53| Round=2 BestEpoch=100 Ac=0.9715 Pr=0.7644 Rc=0.7261 F1=0.7234 Training_time=45.0 s 

|2025-01-30 12:10:49| Round=3 BestEpoch= 61 Ac=0.7527 Pr=0.5898 Rc=0.4282 F1=0.4788 Training_time=27.7 s 

|2025-01-30 12:11:57| Round=4 BestEpoch= 82 Ac=0.8145 Pr=0.7857 Rc=0.5487 F1=0.6035 Training_time=37.4 s 

|2025-01-30 12:13:09| Round=5 BestEpoch= 87 Ac=0.9524 Pr=0.7552 Rc=0.7002 F1=0.6958 Training_time=40.5 s 

|2025-01-30 12:13:09| ********************Experiment Results:********************
|2025-01-30 12:13:09| AC: 0.8628 ± 0.0847
|2025-01-30 12:13:09| PR: 0.7182 ± 0.0708
|2025-01-30 12:13:09| RC: 0.6014 ± 0.1078
|2025-01-30 12:13:09| F1: 0.6148 ± 0.0880
|2025-01-30 12:13:09| train_time: 33.9166 ± 9.4233
|2025-01-30 12:13:11| Flops: 50290688
|2025-01-30 12:13:11| Params: 39878
|2025-01-30 12:13:11| Inference time: 0.81 ms
|2025-01-30 12:13:12| ********************Experiment Success********************
```

