```python
|2025-01-29 00:17:57| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xc49b2e2eb40>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 54, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 00:17:57| ********************Experiment Start********************
|2025-01-29 00:18:54| Round=1 BestEpoch= 57 Ac=0.6615 Pr=0.5931 Rc=0.5774 F1=0.5706 Training_time=29.6 s 

|2025-01-29 00:19:34| Round=2 BestEpoch= 31 Ac=0.6490 Pr=0.5530 Rc=0.5412 F1=0.5409 Training_time=15.8 s 

|2025-01-29 00:19:34| ********************Experiment Results:********************
|2025-01-29 00:19:34| AC: 0.6553 ± 0.0063
|2025-01-29 00:19:34| PR: 0.5731 ± 0.0200
|2025-01-29 00:19:34| RC: 0.5593 ± 0.0181
|2025-01-29 00:19:34| F1: 0.5558 ± 0.0149
|2025-01-29 00:19:34| train_time: 22.7254 ± 6.8757
|2025-01-29 00:19:34| Flops: 145981440
|2025-01-29 00:19:34| Params: 68492
|2025-01-29 00:19:34| Inference time: 0.07 ms
|2025-01-29 00:19:35| ********************Experiment Success********************
```

