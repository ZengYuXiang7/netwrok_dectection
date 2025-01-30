```python
|2025-01-29 21:36:54| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x145999e3e300>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.0025, 'model': graphiot, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 21:36:54| ********************Experiment Start********************
|2025-01-29 21:37:30| Round=1 BestEpoch= 78 Ac=0.7540 Pr=0.4448 Rc=0.4098 F1=0.4169 Training_time=17.1 s 

|2025-01-29 21:38:14| Round=2 BestEpoch= 92 Ac=0.8285 Pr=0.4890 Rc=0.4608 F1=0.4713 Training_time=21.7 s 

|2025-01-29 21:38:14| ********************Experiment Results:********************
|2025-01-29 21:38:14| AC: 0.7913 ± 0.0372
|2025-01-29 21:38:14| PR: 0.4669 ± 0.0221
|2025-01-29 21:38:14| RC: 0.4353 ± 0.0255
|2025-01-29 21:38:14| F1: 0.4441 ± 0.0272
|2025-01-29 21:38:14| train_time: 19.4151 ± 2.2823
|2025-01-29 21:38:14| Flops: 33792512
|2025-01-29 21:38:14| Params: 28670
|2025-01-29 21:38:14| Inference time: 0.81 ms
|2025-01-29 21:38:15| ********************Experiment Success********************
```

