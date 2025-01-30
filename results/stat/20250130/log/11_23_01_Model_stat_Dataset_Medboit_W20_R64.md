```python
|2025-01-30 11:23:01| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xe72ba20f290>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-30 11:23:01| ********************Experiment Start********************
|2025-01-30 11:37:35| Round=1 BestEpoch=146 Ac=0.9405 Pr=0.5692 Rc=0.5382 F1=0.5519 Training_time=38.0 s 

|2025-01-30 11:39:01| Round=2 BestEpoch=160 Ac=0.9417 Pr=0.7644 Rc=0.5664 F1=0.5984 Training_time=41.7 s 

|2025-01-30 11:40:00| Round=3 BestEpoch= 96 Ac=0.9061 Pr=0.7445 Rc=0.5287 F1=0.5732 Training_time=26.1 s 

|2025-01-30 11:41:10| Round=4 BestEpoch=127 Ac=0.9275 Pr=0.4644 Rc=0.4076 F1=0.4259 Training_time=32.9 s 

|2025-01-30 11:42:11| Round=5 BestEpoch=104 Ac=0.9156 Pr=0.4614 Rc=0.3810 F1=0.3974 Training_time=26.7 s 

|2025-01-30 11:42:11| ********************Experiment Results:********************
|2025-01-30 11:42:11| AC: 0.9263 ± 0.0139
|2025-01-30 11:42:11| PR: 0.6008 ± 0.1315
|2025-01-30 11:42:11| RC: 0.4844 ± 0.0751
|2025-01-30 11:42:11| F1: 0.5094 ± 0.0816
|2025-01-30 11:42:11| train_time: 33.0803 ± 6.1140
|2025-01-30 11:42:11| Flops: 202240
|2025-01-30 11:42:11| Params: 3090
|2025-01-30 11:42:11| Inference time: 0.04 ms
|2025-01-30 11:42:12| ********************Experiment Success********************
```

