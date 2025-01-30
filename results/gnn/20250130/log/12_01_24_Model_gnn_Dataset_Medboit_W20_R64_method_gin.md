```python
|2025-01-30 12:01:24| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x99a36cbbef0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 2, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 64, 'record': True,
     'retrain': False, 'rounds': 5, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-30 12:01:24| ********************Experiment Start********************
|2025-01-30 12:01:58| Round=1 BestEpoch= 48 Ac=0.9453 Pr=0.7517 Rc=0.6986 F1=0.6932 Training_time=13.6 s 

|2025-01-30 12:02:35| Round=2 BestEpoch= 53 Ac=0.9489 Pr=0.7555 Rc=0.6640 F1=0.6464 Training_time=16.3 s 

|2025-01-30 12:03:22| Round=3 BestEpoch= 72 Ac=0.9596 Pr=0.6022 Rc=0.6491 F1=0.6216 Training_time=22.4 s 

|2025-01-30 12:03:53| Round=4 BestEpoch= 37 Ac=0.9429 Pr=0.6327 Rc=0.5767 F1=0.5962 Training_time=11.6 s 

|2025-01-30 12:04:31| Round=5 BestEpoch= 51 Ac=0.9441 Pr=0.7999 Rc=0.5975 F1=0.6310 Training_time=15.8 s 

|2025-01-30 12:04:31| ********************Experiment Results:********************
|2025-01-30 12:04:31| AC: 0.9482 ± 0.0060
|2025-01-30 12:04:31| PR: 0.7084 ± 0.0768
|2025-01-30 12:04:31| RC: 0.6372 ± 0.0444
|2025-01-30 12:04:31| F1: 0.6377 ± 0.0322
|2025-01-30 12:04:31| train_time: 15.9422 ± 3.6483
|2025-01-30 12:04:32| Flops: 6144000
|2025-01-30 12:04:32| Params: 12102
|2025-01-30 12:04:32| Inference time: 0.23 ms
|2025-01-30 12:04:33| ********************Experiment Success********************
```

