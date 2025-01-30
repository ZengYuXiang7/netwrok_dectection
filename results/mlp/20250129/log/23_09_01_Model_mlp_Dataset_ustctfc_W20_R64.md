```python
|2025-01-29 23:09:01| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x77831c1bb30>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 10,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 23:09:01| ********************Experiment Start********************
|2025-01-29 23:09:10| Round=1 BestEpoch= 23 Ac=0.8447 Pr=0.4895 Rc=0.4403 F1=0.4569 Training_time=2.3 s 

|2025-01-29 23:09:19| Round=2 BestEpoch= 21 Ac=0.7961 Pr=0.4739 Rc=0.4387 F1=0.4525 Training_time=2.0 s 

|2025-01-29 23:09:39| Round=3 BestEpoch= 95 Ac=0.8091 Pr=0.5270 Rc=0.3949 F1=0.4196 Training_time=9.3 s 

|2025-01-29 23:09:48| Round=4 BestEpoch= 23 Ac=0.8317 Pr=0.5357 Rc=0.4281 F1=0.4557 Training_time=2.2 s 

|2025-01-29 23:10:03| Round=5 BestEpoch= 58 Ac=0.7994 Pr=0.4982 Rc=0.4702 F1=0.4808 Training_time=5.8 s 

|2025-01-29 23:10:20| Round=6 BestEpoch= 74 Ac=0.8544 Pr=0.5425 Rc=0.4698 F1=0.4938 Training_time=7.2 s 

|2025-01-29 23:10:28| Round=7 BestEpoch= 18 Ac=0.7994 Pr=0.4687 Rc=0.4444 F1=0.4517 Training_time=1.8 s 

|2025-01-29 23:10:43| Round=8 BestEpoch= 57 Ac=0.8608 Pr=0.4960 Rc=0.4826 F1=0.4843 Training_time=5.9 s 

|2025-01-29 23:10:51| Round=9 BestEpoch= 18 Ac=0.8414 Pr=0.5132 Rc=0.4870 F1=0.4959 Training_time=1.8 s 

|2025-01-29 23:11:01| Round=10 BestEpoch= 31 Ac=0.8350 Pr=0.5392 Rc=0.4295 F1=0.4574 Training_time=3.1 s 

|2025-01-29 23:11:01| ********************Experiment Results:********************
|2025-01-29 23:11:01| AC: 0.8272 ± 0.0230
|2025-01-29 23:11:01| PR: 0.5084 ± 0.0257
|2025-01-29 23:11:01| RC: 0.4486 ± 0.0272
|2025-01-29 23:11:01| F1: 0.4649 ± 0.0224
|2025-01-29 23:11:01| train_time: 4.1410 ± 2.5653
|2025-01-29 23:11:01| Flops: 910336
|2025-01-29 23:11:01| Params: 6966
|2025-01-29 23:11:01| Inference time: 0.11 ms
|2025-01-29 23:11:04| ********************Experiment Success********************
```

