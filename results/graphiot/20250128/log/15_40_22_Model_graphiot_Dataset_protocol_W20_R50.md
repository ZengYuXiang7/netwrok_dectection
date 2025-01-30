```python
|2025-01-28 15:40:22| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x6c930debb00>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.0025, 'model': graphiot, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 15:40:22| ********************Experiment Start********************
|2025-01-28 15:41:17| Round=1 BestEpoch=137 Ac=0.6095 Pr=0.6707 Rc=0.6383 F1=0.6472 Training_time=28.9 s 

|2025-01-28 15:41:59| Round=2 BestEpoch= 94 Ac=0.6058 Pr=0.6405 Rc=0.5892 F1=0.6008 Training_time=20.5 s 

|2025-01-28 15:41:59| ********************Experiment Results:********************
|2025-01-28 15:41:59| AC: 0.6077 ± 0.0018
|2025-01-28 15:41:59| PR: 0.6556 ± 0.0151
|2025-01-28 15:41:59| RC: 0.6138 ± 0.0245
|2025-01-28 15:41:59| F1: 0.6240 ± 0.0232
|2025-01-28 15:41:59| train_time: 24.6989 ± 4.1521
|2025-01-28 15:42:00| Flops: 31283200
|2025-01-28 15:42:00| Params: 25762
|2025-01-28 15:42:00| Inference time: 0.85 ms
|2025-01-28 15:42:00| ********************Experiment Success********************
```

