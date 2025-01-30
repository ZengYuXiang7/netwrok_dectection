```python
|2025-01-29 20:35:00| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 10, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x1491b9587bf0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 20:35:00| ********************Experiment Start********************
|2025-01-29 20:35:00| Ac=0.8768 Pr=0.7621 Rc=0.7389 F1=0.7347 time=30.9 s 
|2025-01-29 20:35:00| Ac=0.8504 Pr=0.6664 Rc=0.5671 F1=0.6006 time=12.0 s 
|2025-01-29 20:35:00| ********************Experiment Results:********************
|2025-01-29 20:35:00| AC: 0.8636 ± 0.0132
|2025-01-29 20:35:00| PR: 0.7142 ± 0.0478
|2025-01-29 20:35:00| RC: 0.6530 ± 0.0859
|2025-01-29 20:35:00| F1: 0.6677 ± 0.0671
|2025-01-29 20:35:00| train_time: 21.4807 ± 9.4671
|2025-01-29 20:35:01| Flops: 11301888
|2025-01-29 20:35:01| Params: 9481
|2025-01-29 20:35:01| Inference time: 0.10 ms
|2025-01-29 20:35:01| ********************Experiment Success********************
```

