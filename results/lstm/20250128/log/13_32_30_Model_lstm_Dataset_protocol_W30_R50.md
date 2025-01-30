```python
|2025-01-28 13:32:30| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x13c0a099f710>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 13:32:30| ********************Experiment Start********************
|2025-01-28 13:32:49| Round=1 BestEpoch= 73 Ac=0.6089 Pr=0.7079 Rc=0.6534 F1=0.6673 Training_time=7.3 s 

|2025-01-28 13:33:02| Round=2 BestEpoch= 45 Ac=0.6436 Pr=0.7571 Rc=0.6473 F1=0.6664 Training_time=4.3 s 

|2025-01-28 13:33:02| ********************Experiment Results:********************
|2025-01-28 13:33:02| AC: 0.6262 ± 0.0173
|2025-01-28 13:33:02| PR: 0.7325 ± 0.0246
|2025-01-28 13:33:02| RC: 0.6503 ± 0.0030
|2025-01-28 13:33:02| F1: 0.6669 ± 0.0004
|2025-01-28 13:33:02| train_time: 5.8165 ± 1.5257
|2025-01-28 13:33:02| Flops: 124416000
|2025-01-28 13:33:02| Params: 49012
|2025-01-28 13:33:02| Inference time: 0.07 ms
|2025-01-28 13:33:02| ********************Experiment Success********************
```

