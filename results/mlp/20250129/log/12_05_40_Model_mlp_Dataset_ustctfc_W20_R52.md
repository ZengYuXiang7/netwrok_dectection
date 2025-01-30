```python
|2025-01-29 12:05:40| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x11e629c3ecc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 12:05:40| ********************Experiment Start********************
|2025-01-29 12:07:12| Round=1 BestEpoch=131 Ac=0.6128 Pr=0.4810 Rc=0.4727 F1=0.4670 Training_time=57.9 s 

|2025-01-29 12:07:52| Round=2 BestEpoch= 36 Ac=0.6123 Pr=0.4620 Rc=0.4107 F1=0.4137 Training_time=16.9 s 

|2025-01-29 12:07:52| ********************Experiment Results:********************
|2025-01-29 12:07:52| AC: 0.6126 ± 0.0002
|2025-01-29 12:07:52| PR: 0.4715 ± 0.0095
|2025-01-29 12:07:52| RC: 0.4417 ± 0.0310
|2025-01-29 12:07:52| F1: 0.4403 ± 0.0267
|2025-01-29 12:07:52| train_time: 37.4002 ± 20.4914
|2025-01-29 12:07:52| Flops: 675840
|2025-01-29 12:07:52| Params: 5156
|2025-01-29 12:07:52| Inference time: 0.06 ms
|2025-01-29 12:07:52| ********************Experiment Success********************
```

