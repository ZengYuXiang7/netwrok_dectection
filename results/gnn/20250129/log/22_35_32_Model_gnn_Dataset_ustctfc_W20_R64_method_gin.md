```python
|2025-01-29 22:35:32| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xb63488ab530>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 2, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 64, 'record': True,
     'retrain': False, 'rounds': 5, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 22:35:32| ********************Experiment Start********************
|2025-01-29 22:36:17| Round=1 BestEpoch=148 Ac=0.8608 Pr=0.4640 Rc=0.4484 F1=0.4517 Training_time=22.9 s 

|2025-01-29 22:37:04| Round=2 BestEpoch=146 Ac=0.8706 Pr=0.4494 Rc=0.4280 F1=0.4344 Training_time=23.7 s 

|2025-01-29 22:37:36| Round=3 BestEpoch= 88 Ac=0.8544 Pr=0.4925 Rc=0.4454 F1=0.4610 Training_time=14.7 s 

|2025-01-29 22:38:05| Round=4 BestEpoch= 72 Ac=0.8544 Pr=0.4772 Rc=0.4437 F1=0.4560 Training_time=12.4 s 

|2025-01-29 22:38:36| Round=5 BestEpoch= 83 Ac=0.8544 Pr=0.4452 Rc=0.4451 F1=0.4436 Training_time=14.1 s 

|2025-01-29 22:38:36| ********************Experiment Results:********************
|2025-01-29 22:38:36| AC: 0.8589 ± 0.0063
|2025-01-29 22:38:36| PR: 0.4657 ± 0.0176
|2025-01-29 22:38:36| RC: 0.4421 ± 0.0072
|2025-01-29 22:38:36| F1: 0.4493 ± 0.0094
|2025-01-29 22:38:36| train_time: 17.5757 ± 4.7749
|2025-01-29 22:38:37| Flops: 7127040
|2025-01-29 22:38:37| Params: 27474
|2025-01-29 22:38:37| Inference time: 0.23 ms
|2025-01-29 22:38:38| ********************Experiment Success********************
```

