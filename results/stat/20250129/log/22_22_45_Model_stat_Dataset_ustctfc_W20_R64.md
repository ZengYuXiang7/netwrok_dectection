```python
|2025-01-29 22:22:45| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x5e8b5698bf0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 22:22:45| ********************Experiment Start********************
|2025-01-29 22:24:09| Round=1 BestEpoch= 57 Ac=0.6278 Pr=0.2711 Rc=0.2583 F1=0.2568 Training_time=6.5 s 

|2025-01-29 22:24:30| Round=2 BestEpoch= 81 Ac=0.5955 Pr=0.2470 Rc=0.2397 F1=0.2393 Training_time=8.8 s 

|2025-01-29 22:25:07| Round=3 BestEpoch=167 Ac=0.6084 Pr=0.3861 Rc=0.3065 F1=0.3207 Training_time=18.5 s 

|2025-01-29 22:25:27| Round=4 BestEpoch= 79 Ac=0.6343 Pr=0.3713 Rc=0.2871 F1=0.3003 Training_time=8.6 s 

|2025-01-29 22:25:40| Round=5 BestEpoch= 37 Ac=0.5631 Pr=0.2302 Rc=0.2287 F1=0.2267 Training_time=4.0 s 

|2025-01-29 22:25:40| ********************Experiment Results:********************
|2025-01-29 22:25:40| AC: 0.6058 ± 0.0254
|2025-01-29 22:25:40| PR: 0.3012 ± 0.0648
|2025-01-29 22:25:40| RC: 0.2641 ± 0.0290
|2025-01-29 22:25:40| F1: 0.2688 ± 0.0360
|2025-01-29 22:25:40| train_time: 9.2651 ± 4.9138
|2025-01-29 22:25:40| Flops: 254464
|2025-01-29 22:25:40| Params: 3894
|2025-01-29 22:25:40| Inference time: 0.04 ms
|2025-01-29 22:25:41| ********************Experiment Success********************
```

