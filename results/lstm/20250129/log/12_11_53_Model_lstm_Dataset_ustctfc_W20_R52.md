```python
|2025-01-29 12:11:53| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xad532166cc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 12:11:53| ********************Experiment Start********************
|2025-01-29 12:13:33| Round=1 BestEpoch=115 Ac=0.6144 Pr=0.5337 Rc=0.4792 F1=0.4848 Training_time=61.7 s 

|2025-01-29 12:14:43| Round=2 BestEpoch= 64 Ac=0.6139 Pr=0.5030 Rc=0.5274 F1=0.5041 Training_time=37.8 s 

|2025-01-29 12:14:43| ********************Experiment Results:********************
|2025-01-29 12:14:43| AC: 0.6141 ± 0.0002
|2025-01-29 12:14:43| PR: 0.5183 ± 0.0153
|2025-01-29 12:14:43| RC: 0.5033 ± 0.0241
|2025-01-29 12:14:43| F1: 0.4944 ± 0.0097
|2025-01-29 12:14:43| train_time: 49.7488 ± 11.9076
|2025-01-29 12:14:43| Flops: 90521600
|2025-01-29 12:14:43| Params: 54308
|2025-01-29 12:14:43| Inference time: 0.07 ms
|2025-01-29 12:14:44| ********************Experiment Success********************
```

