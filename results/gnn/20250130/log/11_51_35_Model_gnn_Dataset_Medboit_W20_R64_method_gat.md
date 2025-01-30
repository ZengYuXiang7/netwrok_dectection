```python
|2025-01-30 11:51:35| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0x6ef84b1e030>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 5, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-30 11:51:35| ********************Experiment Start********************
|2025-01-30 11:53:28| Round=1 BestEpoch=135 Ac=0.9489 Pr=0.7071 Rc=0.7017 F1=0.6836 Training_time=71.1 s 

|2025-01-30 11:55:35| Round=2 BestEpoch=145 Ac=0.9774 Pr=0.8185 Rc=0.7290 F1=0.7559 Training_time=81.1 s 

|2025-01-30 11:57:10| Round=3 BestEpoch= 99 Ac=0.9715 Pr=0.7802 Rc=0.7273 F1=0.7452 Training_time=56.4 s 

|2025-01-30 11:59:44| Round=4 BestEpoch=178 Ac=0.9750 Pr=0.8146 Rc=0.7106 F1=0.7348 Training_time=100.4 s 

|2025-01-30 12:01:19| Round=5 BestEpoch= 99 Ac=0.9727 Pr=0.8135 Rc=0.7097 F1=0.7338 Training_time=55.9 s 

|2025-01-30 12:01:19| ********************Experiment Results:********************
|2025-01-30 12:01:19| AC: 0.9691 ± 0.0103
|2025-01-30 12:01:19| PR: 0.7868 ± 0.0422
|2025-01-30 12:01:19| RC: 0.7156 ± 0.0107
|2025-01-30 12:01:19| F1: 0.7306 ± 0.0249
|2025-01-30 12:01:19| train_time: 72.9692 ± 16.6502
|2025-01-30 12:01:21| Flops: 33013760
|2025-01-30 12:01:21| Params: 32774
|2025-01-30 12:01:21| Inference time: 1.40 ms
|2025-01-30 12:01:22| ********************Experiment Success********************
```

