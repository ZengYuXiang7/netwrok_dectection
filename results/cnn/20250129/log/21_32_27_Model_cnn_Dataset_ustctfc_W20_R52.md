```python
|2025-01-29 21:32:27| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xdc85ce86cc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 21:32:27| ********************Experiment Start********************
|2025-01-29 21:33:00| Round=1 BestEpoch=131 Ac=0.8350 Pr=0.4669 Rc=0.4383 F1=0.4483 Training_time=14.3 s 

|2025-01-29 21:33:17| Round=2 BestEpoch= 56 Ac=0.8026 Pr=0.3280 Rc=0.3391 F1=0.3324 Training_time=6.0 s 

|2025-01-29 21:33:17| ********************Experiment Results:********************
|2025-01-29 21:33:17| AC: 0.8188 ± 0.0162
|2025-01-29 21:33:17| PR: 0.3974 ± 0.0695
|2025-01-29 21:33:17| RC: 0.3887 ± 0.0496
|2025-01-29 21:33:17| F1: 0.3904 ± 0.0580
|2025-01-29 21:33:17| train_time: 10.1869 ± 4.1553
|2025-01-29 21:33:17| Flops: 22490624
|2025-01-29 21:33:17| Params: 9534
|2025-01-29 21:33:17| Inference time: 0.09 ms
|2025-01-29 21:33:18| ********************Experiment Success********************
```

