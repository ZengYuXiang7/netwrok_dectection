```python
|2025-01-30 13:12:08| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xafc9cfe5730>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-30 13:12:08| ********************Experiment Start********************
|2025-01-30 13:12:47| Round=1 BestEpoch= 32 Ac=0.9927 Pr=0.5387 Rc=0.4962 F1=0.5089 Training_time=15.8 s 

|2025-01-30 13:13:15| Round=2 BestEpoch= 14 Ac=0.9942 Pr=0.5534 Rc=0.5274 F1=0.5351 Training_time=6.8 s 

|2025-01-30 13:13:43| Round=3 BestEpoch= 16 Ac=0.9939 Pr=0.5051 Rc=0.5098 F1=0.5064 Training_time=7.7 s 

|2025-01-30 13:14:21| Round=4 BestEpoch= 30 Ac=0.9914 Pr=0.5772 Rc=0.4554 F1=0.4791 Training_time=14.4 s 

|2025-01-30 13:14:46| Round=5 BestEpoch= 10 Ac=0.9933 Pr=0.5248 Rc=0.5277 F1=0.5185 Training_time=5.0 s 

|2025-01-30 13:14:46| ********************Experiment Results:********************
|2025-01-30 13:14:46| AC: 0.9931 ± 0.0010
|2025-01-30 13:14:46| PR: 0.5399 ± 0.0245
|2025-01-30 13:14:46| RC: 0.5033 ± 0.0267
|2025-01-30 13:14:46| F1: 0.5096 ± 0.0183
|2025-01-30 13:14:46| train_time: 9.9366 ± 4.3232
|2025-01-30 13:14:46| Flops: 849408
|2025-01-30 13:14:46| Params: 6497
|2025-01-30 13:14:46| Inference time: 0.06 ms
|2025-01-30 13:14:47| ********************Experiment Success********************
```

