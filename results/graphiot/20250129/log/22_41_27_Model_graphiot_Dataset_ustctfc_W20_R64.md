```python
|2025-01-29 22:41:27| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x1120c2154770>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.0025, 'model': graphiot, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 22:41:27| ********************Experiment Start********************
|2025-01-29 22:42:19| Round=1 BestEpoch=137 Ac=0.8641 Pr=0.5495 Rc=0.4499 F1=0.4734 Training_time=28.3 s 

|2025-01-29 22:43:01| Round=2 BestEpoch= 99 Ac=0.8706 Pr=0.4939 Rc=0.4764 F1=0.4809 Training_time=21.9 s 

|2025-01-29 22:43:41| Round=3 BestEpoch= 89 Ac=0.5987 Pr=0.3902 Rc=0.3561 F1=0.3327 Training_time=19.8 s 

|2025-01-29 22:44:17| Round=4 BestEpoch= 79 Ac=0.6699 Pr=0.4206 Rc=0.4119 F1=0.3965 Training_time=17.7 s 

|2025-01-29 22:44:46| Round=5 BestEpoch= 55 Ac=0.6052 Pr=0.3877 Rc=0.4053 F1=0.3475 Training_time=12.4 s 

|2025-01-29 22:44:46| ********************Experiment Results:********************
|2025-01-29 22:44:46| AC: 0.7217 ± 0.1215
|2025-01-29 22:44:46| PR: 0.4484 ± 0.0635
|2025-01-29 22:44:46| RC: 0.4199 ± 0.0411
|2025-01-29 22:44:46| F1: 0.4062 ± 0.0617
|2025-01-29 22:44:46| train_time: 20.0390 ± 5.2098
|2025-01-29 22:44:47| Flops: 50438144
|2025-01-29 22:44:47| Params: 42194
|2025-01-29 22:44:47| Inference time: 0.81 ms
|2025-01-29 22:44:48| ********************Experiment Success********************
```

