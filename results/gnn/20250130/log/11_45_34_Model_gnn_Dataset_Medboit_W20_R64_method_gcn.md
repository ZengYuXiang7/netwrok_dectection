```python
|2025-01-30 11:45:34| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xfd96a0900e0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 64, 'record': True,
     'retrain': False, 'rounds': 5, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-30 11:45:34| ********************Experiment Start********************
|2025-01-30 11:46:44| Round=1 BestEpoch= 62 Ac=0.9655 Pr=0.7473 Rc=0.7067 F1=0.6919 Training_time=25.4 s 

|2025-01-30 11:47:40| Round=2 BestEpoch= 64 Ac=0.9608 Pr=0.7571 Rc=0.7051 F1=0.6992 Training_time=28.1 s 

|2025-01-30 11:49:10| Round=3 BestEpoch=119 Ac=0.9655 Pr=0.7616 Rc=0.7246 F1=0.7213 Training_time=52.8 s 

|2025-01-30 11:50:22| Round=4 BestEpoch= 90 Ac=0.9667 Pr=0.7290 Rc=0.7252 F1=0.7146 Training_time=39.6 s 

|2025-01-30 11:51:30| Round=5 BestEpoch= 80 Ac=0.9631 Pr=0.7607 Rc=0.7237 F1=0.7204 Training_time=36.6 s 

|2025-01-30 11:51:30| ********************Experiment Results:********************
|2025-01-30 11:51:30| AC: 0.9643 ± 0.0021
|2025-01-30 11:51:30| PR: 0.7511 ± 0.0122
|2025-01-30 11:51:30| RC: 0.7171 ± 0.0092
|2025-01-30 11:51:30| F1: 0.7095 ± 0.0118
|2025-01-30 11:51:30| train_time: 36.4865 ± 9.6802
|2025-01-30 11:51:31| Flops: 1556480
|2025-01-30 11:51:31| Params: 8198
|2025-01-30 11:51:31| Inference time: 1.15 ms
|2025-01-30 11:51:33| ********************Experiment Success********************
```

