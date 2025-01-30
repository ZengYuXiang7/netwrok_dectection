```python
|2025-01-29 23:15:23| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x119bf6ca6f90>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 10,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 23:15:23| ********************Experiment Start********************
|2025-01-29 23:15:41| Round=1 BestEpoch= 57 Ac=0.6278 Pr=0.2711 Rc=0.2583 F1=0.2568 Training_time=6.7 s 

|2025-01-29 23:16:04| Round=2 BestEpoch= 81 Ac=0.5955 Pr=0.2470 Rc=0.2397 F1=0.2393 Training_time=9.5 s 

|2025-01-29 23:16:43| Round=3 BestEpoch=167 Ac=0.6084 Pr=0.3861 Rc=0.3065 F1=0.3207 Training_time=19.6 s 

|2025-01-29 23:17:05| Round=4 BestEpoch= 79 Ac=0.6343 Pr=0.3713 Rc=0.2871 F1=0.3003 Training_time=9.2 s 

|2025-01-29 23:17:18| Round=5 BestEpoch= 37 Ac=0.5631 Pr=0.2302 Rc=0.2287 F1=0.2267 Training_time=4.4 s 

|2025-01-29 23:17:45| Round=6 BestEpoch=100 Ac=0.6667 Pr=0.3869 Rc=0.3355 F1=0.3480 Training_time=11.9 s 

|2025-01-29 23:18:09| Round=7 BestEpoch= 91 Ac=0.6149 Pr=0.4085 Rc=0.3347 F1=0.3305 Training_time=10.6 s 

|2025-01-29 23:18:29| Round=8 BestEpoch= 69 Ac=0.6667 Pr=0.2748 Rc=0.2723 F1=0.2699 Training_time=8.1 s 

|2025-01-29 23:18:42| Round=9 BestEpoch= 36 Ac=0.4660 Pr=0.2460 Rc=0.2460 F1=0.2161 Training_time=4.2 s 

|2025-01-29 23:19:11| Round=10 BestEpoch=114 Ac=0.5599 Pr=0.3225 Rc=0.2827 F1=0.2963 Training_time=13.3 s 

|2025-01-29 23:19:11| ********************Experiment Results:********************
|2025-01-29 23:19:11| AC: 0.6003 ± 0.0566
|2025-01-29 23:19:11| PR: 0.3144 ± 0.0650
|2025-01-29 23:19:11| RC: 0.2792 ± 0.0357
|2025-01-29 23:19:11| F1: 0.2805 ± 0.0433
|2025-01-29 23:19:11| train_time: 9.7329 ± 4.3047
|2025-01-29 23:19:11| Flops: 254464
|2025-01-29 23:19:11| Params: 3894
|2025-01-29 23:19:11| Inference time: 0.04 ms
|2025-01-29 23:19:14| ********************Experiment Success********************
```

