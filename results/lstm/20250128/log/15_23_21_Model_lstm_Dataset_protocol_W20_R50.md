```python
|2025-01-28 15:23:21| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x7b80dd640e0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 15:23:21| ********************Experiment Start********************
|2025-01-28 15:23:37| Round=1 BestEpoch= 41 Ac=0.6204 Pr=0.5952 Rc=0.6083 F1=0.5939 Training_time=4.7 s 

|2025-01-28 15:24:10| Round=2 BestEpoch=128 Ac=0.6825 Pr=0.7197 Rc=0.6998 F1=0.7069 Training_time=14.3 s 

|2025-01-28 15:24:10| ********************Experiment Results:********************
|2025-01-28 15:24:10| AC: 0.6515 ± 0.0310
|2025-01-28 15:24:10| PR: 0.6575 ± 0.0622
|2025-01-28 15:24:10| RC: 0.6540 ± 0.0458
|2025-01-28 15:24:10| F1: 0.6504 ± 0.0565
|2025-01-28 15:24:10| train_time: 9.5433 ± 4.8033
|2025-01-28 15:24:10| Flops: 82944000
|2025-01-28 15:24:10| Params: 43012
|2025-01-28 15:24:10| Inference time: 0.07 ms
|2025-01-28 15:24:10| ********************Experiment Success********************
```

