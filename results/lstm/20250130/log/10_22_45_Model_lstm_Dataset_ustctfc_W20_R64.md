```python
|2025-01-30 10:22:45| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x10e6980a6c60>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-30 10:22:45| ********************Experiment Start********************
|2025-01-30 10:23:37| Round=1 BestEpoch=109 Ac=0.9853 Pr=0.5442 Rc=0.5285 F1=0.5314 Training_time=30.1 s 

|2025-01-30 10:24:21| Round=2 BestEpoch= 86 Ac=0.9870 Pr=0.5932 Rc=0.6379 F1=0.5831 Training_time=23.5 s 

|2025-01-30 10:24:52| Round=3 BestEpoch= 51 Ac=0.9839 Pr=0.5884 Rc=0.5454 F1=0.5580 Training_time=14.5 s 

|2025-01-30 10:25:28| Round=4 BestEpoch= 64 Ac=0.9842 Pr=0.5139 Rc=0.5465 F1=0.5268 Training_time=17.5 s 

|2025-01-30 10:26:01| Round=5 BestEpoch= 58 Ac=0.9866 Pr=0.5612 Rc=0.5331 F1=0.5219 Training_time=16.0 s 

|2025-01-30 10:26:01| ********************Experiment Results:********************
|2025-01-30 10:26:01| AC: 0.9854 ± 0.0012
|2025-01-30 10:26:01| PR: 0.5602 ± 0.0293
|2025-01-30 10:26:01| RC: 0.5583 ± 0.0404
|2025-01-30 10:26:01| F1: 0.5442 ± 0.0231
|2025-01-30 10:26:01| train_time: 20.3243 ± 5.7572
|2025-01-30 10:26:01| Flops: 134840320
|2025-01-30 10:26:01| Params: 74771
|2025-01-30 10:26:01| Inference time: 0.08 ms
|2025-01-30 10:26:02| ********************Experiment Success********************
```

