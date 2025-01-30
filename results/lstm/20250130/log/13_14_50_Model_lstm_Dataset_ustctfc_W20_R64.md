```python
|2025-01-30 13:14:50| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xc5093ec63f0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-30 13:14:50| ********************Experiment Start********************
|2025-01-30 13:16:01| Round=1 BestEpoch= 76 Ac=0.9945 Pr=0.6023 Rc=0.5525 F1=0.5718 Training_time=41.3 s 

|2025-01-30 13:16:26| Round=2 BestEpoch= 10 Ac=0.9956 Pr=0.5615 Rc=0.5809 F1=0.5694 Training_time=5.1 s 

|2025-01-30 13:16:57| Round=3 BestEpoch= 18 Ac=0.9958 Pr=0.6090 Rc=0.5888 F1=0.5966 Training_time=9.0 s 

|2025-01-30 13:17:29| Round=4 BestEpoch= 19 Ac=0.9930 Pr=0.5379 Rc=0.5487 F1=0.5394 Training_time=10.3 s 

|2025-01-30 13:18:08| Round=5 BestEpoch= 31 Ac=0.9941 Pr=0.5561 Rc=0.5349 F1=0.5405 Training_time=15.7 s 

|2025-01-30 13:18:08| ********************Experiment Results:********************
|2025-01-30 13:18:08| AC: 0.9946 ± 0.0010
|2025-01-30 13:18:08| PR: 0.5734 ± 0.0276
|2025-01-30 13:18:08| RC: 0.5611 ± 0.0203
|2025-01-30 13:18:08| F1: 0.5635 ± 0.0215
|2025-01-30 13:18:08| train_time: 16.2664 ± 12.9539
|2025-01-30 13:18:08| Flops: 133529600
|2025-01-30 13:18:08| Params: 64523
|2025-01-30 13:18:08| Inference time: 0.07 ms
|2025-01-30 13:18:10| ********************Experiment Success********************
```

