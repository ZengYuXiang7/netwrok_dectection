```python
|2025-01-30 10:20:41| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xb28ac7a0050>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-30 10:20:41| ********************Experiment Start********************
|2025-01-30 10:21:00| Round=1 BestEpoch= 25 Ac=0.9815 Pr=0.5430 Rc=0.5372 F1=0.5385 Training_time=6.1 s 

|2025-01-30 10:21:27| Round=2 BestEpoch= 51 Ac=0.9860 Pr=0.5604 Rc=0.5216 F1=0.5361 Training_time=12.4 s 

|2025-01-30 10:21:45| Round=3 BestEpoch= 22 Ac=0.9791 Pr=0.4977 Rc=0.5280 F1=0.5026 Training_time=5.3 s 

|2025-01-30 10:22:13| Round=4 BestEpoch= 51 Ac=0.9825 Pr=0.5383 Rc=0.5599 F1=0.5384 Training_time=12.4 s 

|2025-01-30 10:22:41| Round=5 BestEpoch= 53 Ac=0.9836 Pr=0.5417 Rc=0.4621 F1=0.4813 Training_time=13.0 s 

|2025-01-30 10:22:41| ********************Experiment Results:********************
|2025-01-30 10:22:41| AC: 0.9825 ± 0.0023
|2025-01-30 10:22:41| PR: 0.5362 ± 0.0207
|2025-01-30 10:22:41| RC: 0.5218 ± 0.0325
|2025-01-30 10:22:41| F1: 0.5194 ± 0.0234
|2025-01-30 10:22:41| train_time: 9.8338 ± 3.4172
|2025-01-30 10:22:41| Flops: 919040
|2025-01-30 10:22:41| Params: 7033
|2025-01-30 10:22:41| Inference time: 0.06 ms
|2025-01-30 10:22:42| ********************Experiment Success********************
```

