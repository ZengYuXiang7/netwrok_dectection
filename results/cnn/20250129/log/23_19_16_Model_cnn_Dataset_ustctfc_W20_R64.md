```python
|2025-01-29 23:19:16| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xf048ee13bc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 10,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 23:19:16| ********************Experiment Start********************
|2025-01-29 23:19:52| Round=1 BestEpoch=158 Ac=0.8576 Pr=0.4984 Rc=0.4470 F1=0.4649 Training_time=17.7 s 

|2025-01-29 23:20:20| Round=2 BestEpoch=117 Ac=0.8350 Pr=0.4151 Rc=0.4214 F1=0.4163 Training_time=12.8 s 

|2025-01-29 23:20:46| Round=3 BestEpoch=108 Ac=0.8317 Pr=0.4813 Rc=0.4284 F1=0.4361 Training_time=12.0 s 

|2025-01-29 23:21:10| Round=4 BestEpoch=100 Ac=0.8511 Pr=0.4464 Rc=0.4052 F1=0.4146 Training_time=11.1 s 

|2025-01-29 23:21:52| Round=5 BestEpoch=185 Ac=0.8641 Pr=0.4694 Rc=0.4401 F1=0.4503 Training_time=21.3 s 

|2025-01-29 23:22:20| Round=6 BestEpoch=119 Ac=0.8350 Pr=0.4404 Rc=0.4226 F1=0.4280 Training_time=13.3 s 

|2025-01-29 23:22:54| Round=7 BestEpoch=147 Ac=0.8317 Pr=0.4830 Rc=0.4592 F1=0.4658 Training_time=16.5 s 

|2025-01-29 23:23:14| Round=8 BestEpoch= 73 Ac=0.8382 Pr=0.3401 Rc=0.3525 F1=0.3456 Training_time=8.1 s 

|2025-01-29 23:23:40| Round=9 BestEpoch=106 Ac=0.8317 Pr=0.3894 Rc=0.3968 F1=0.3905 Training_time=11.9 s 

|2025-01-29 23:23:58| Round=10 BestEpoch= 66 Ac=0.8155 Pr=0.4331 Rc=0.3684 F1=0.3748 Training_time=7.3 s 

|2025-01-29 23:23:58| ********************Experiment Results:********************
|2025-01-29 23:23:58| AC: 0.8392 ± 0.0137
|2025-01-29 23:23:58| PR: 0.4397 ± 0.0459
|2025-01-29 23:23:58| RC: 0.4141 ± 0.0322
|2025-01-29 23:23:58| F1: 0.4187 ± 0.0372
|2025-01-29 23:23:58| train_time: 13.2081 ± 4.0573
|2025-01-29 23:23:58| Flops: 33579008
|2025-01-29 23:23:58| Params: 14034
|2025-01-29 23:23:58| Inference time: 0.09 ms
|2025-01-29 23:24:00| ********************Experiment Success********************
```

