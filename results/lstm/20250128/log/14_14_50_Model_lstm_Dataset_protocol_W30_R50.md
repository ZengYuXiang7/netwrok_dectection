```python
|2025-01-28 14:14:50| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xc88f8a95970>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 14:14:50| ********************Experiment Start********************
|2025-01-28 14:15:17| Round=1 BestEpoch=111 Ac=0.4720 Pr=0.4911 Rc=0.4324 F1=0.4390 Training_time=12.0 s 

|2025-01-28 14:15:43| Round=2 BestEpoch=105 Ac=0.5514 Pr=0.6398 Rc=0.5347 F1=0.5594 Training_time=11.2 s 

|2025-01-28 14:15:43| ********************Experiment Results:********************
|2025-01-28 14:15:43| AC: 0.5117 ± 0.0397
|2025-01-28 14:15:43| PR: 0.5654 ± 0.0744
|2025-01-28 14:15:43| RC: 0.4835 ± 0.0512
|2025-01-28 14:15:43| F1: 0.4992 ± 0.0602
|2025-01-28 14:15:43| train_time: 11.6117 ± 0.4047
|2025-01-28 14:15:43| Flops: 127296000
|2025-01-28 14:15:43| Params: 71527
|2025-01-28 14:15:43| Inference time: 0.07 ms
|2025-01-28 14:15:44| ********************Experiment Success********************
```

