```python
|2025-01-27 18:40:48| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0x143351165730>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-27 18:40:48| ********************Experiment Start********************
|2025-01-27 18:58:44| Round=1 BestEpoch=186 Ac=0.8813 Pr=0.8177 Rc=0.8105 F1=0.8121   Training_time=817.8 s 

|2025-01-27 18:58:44| ********************Experiment Results:********************
|2025-01-27 18:58:44| AC: 0.8813 ± 0.0000
|2025-01-27 18:58:44| PR: 0.8177 ± 0.0000
|2025-01-27 18:58:44| RC: 0.8105 ± 0.0000
|2025-01-27 18:58:44| F1: 0.8121 ± 0.0000
|2025-01-27 18:58:44| train_time: 817.8018 ± 0.0000
|2025-01-27 18:58:59| Flops: 32064000
|2025-01-27 18:58:59| Params: 46921
|2025-01-27 18:58:59| Inference time: 1.51 ms
|2025-01-27 18:59:00| ********************Experiment Success********************
```

