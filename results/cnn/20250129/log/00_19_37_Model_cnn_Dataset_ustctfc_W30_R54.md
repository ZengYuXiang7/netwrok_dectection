```python
|2025-01-29 00:19:37| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xfe5045a6ea0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 54, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 00:19:37| ********************Experiment Start********************
|2025-01-29 00:20:22| Round=1 BestEpoch= 38 Ac=0.6175 Pr=0.5532 Rc=0.5214 F1=0.5038 Training_time=19.1 s 

|2025-01-29 00:21:15| Round=2 BestEpoch= 52 Ac=0.6161 Pr=0.5821 Rc=0.5044 F1=0.5213 Training_time=26.0 s 

|2025-01-29 00:21:15| ********************Experiment Results:********************
|2025-01-29 00:21:15| AC: 0.6168 ± 0.0007
|2025-01-29 00:21:15| PR: 0.5676 ± 0.0145
|2025-01-29 00:21:15| RC: 0.5129 ± 0.0085
|2025-01-29 00:21:15| F1: 0.5125 ± 0.0087
|2025-01-29 00:21:15| train_time: 22.5437 ± 3.4071
|2025-01-29 00:21:15| Flops: 36225792
|2025-01-29 00:21:15| Params: 10334
|2025-01-29 00:21:15| Inference time: 0.10 ms
|2025-01-29 00:21:16| ********************Experiment Success********************
```

