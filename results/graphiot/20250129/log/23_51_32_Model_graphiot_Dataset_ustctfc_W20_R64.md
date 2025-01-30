```python
|2025-01-29 23:51:32| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xcd21d898350>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.0025, 'model': graphiot, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 10,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 23:51:32| ********************Experiment Start********************
|2025-01-29 23:52:29| Round=1 BestEpoch=137 Ac=0.8641 Pr=0.5495 Rc=0.4499 F1=0.4734 Training_time=30.9 s 

|2025-01-29 23:53:15| Round=2 BestEpoch= 99 Ac=0.8706 Pr=0.4939 Rc=0.4764 F1=0.4809 Training_time=23.5 s 

|2025-01-29 23:53:58| Round=3 BestEpoch= 89 Ac=0.5987 Pr=0.3902 Rc=0.3561 F1=0.3327 Training_time=21.5 s 

|2025-01-29 23:54:37| Round=4 BestEpoch= 79 Ac=0.6699 Pr=0.4206 Rc=0.4119 F1=0.3965 Training_time=19.1 s 

|2025-01-29 23:55:08| Round=5 BestEpoch= 55 Ac=0.6052 Pr=0.3877 Rc=0.4053 F1=0.3475 Training_time=13.2 s 

|2025-01-29 23:56:16| Round=6 BestEpoch=170 Ac=0.8706 Pr=0.4909 Rc=0.4526 F1=0.4674 Training_time=39.2 s 

|2025-01-29 23:57:17| Round=7 BestEpoch=152 Ac=0.8641 Pr=0.5018 Rc=0.4734 F1=0.4837 Training_time=33.9 s 

|2025-01-29 23:57:57| Round=8 BestEpoch= 92 Ac=0.8641 Pr=0.4924 Rc=0.4741 F1=0.4785 Training_time=20.4 s 

|2025-01-29 23:58:17| Round=9 BestEpoch= 27 Ac=0.7735 Pr=0.4509 Rc=0.4406 F1=0.4397 Training_time=6.1 s 

|2025-01-29 23:59:02| Round=10 BestEpoch=106 Ac=0.8641 Pr=0.4772 Rc=0.4503 F1=0.4596 Training_time=23.4 s 

|2025-01-29 23:59:02| ********************Experiment Results:********************
|2025-01-29 23:59:02| AC: 0.7845 ± 0.1096
|2025-01-29 23:59:02| PR: 0.4655 ± 0.0496
|2025-01-29 23:59:02| RC: 0.4391 ± 0.0360
|2025-01-29 23:59:02| F1: 0.4360 ± 0.0540
|2025-01-29 23:59:02| train_time: 23.1284 ± 9.2200
|2025-01-29 23:59:02| Flops: 50438144
|2025-01-29 23:59:02| Params: 42194
|2025-01-29 23:59:02| Inference time: 0.82 ms
|2025-01-29 23:59:05| ********************Experiment Success********************
```

