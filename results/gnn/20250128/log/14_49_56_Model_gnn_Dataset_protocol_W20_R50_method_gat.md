```python
|2025-01-28 14:49:56| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0x112974dc1400>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-28 14:49:56| ********************Experiment Start********************
|2025-01-28 14:50:23| Round=1 BestEpoch= 41 Ac=0.5795 Pr=0.5516 Rc=0.5279 F1=0.5141 Training_time=10.4 s 

|2025-01-28 14:50:23| ********************Experiment Results:********************
|2025-01-28 14:50:23| AC: 0.5795 ± 0.0000
|2025-01-28 14:50:23| PR: 0.5516 ± 0.0000
|2025-01-28 14:50:23| RC: 0.5279 ± 0.0000
|2025-01-28 14:50:23| F1: 0.5141 ± 0.0000
|2025-01-28 14:50:23| train_time: 10.3815 ± 0.0000
|2025-01-28 14:50:24| Flops: 21760000
|2025-01-28 14:50:24| Params: 42427
|2025-01-28 14:50:24| Inference time: 1.42 ms
|2025-01-28 14:50:25| ********************Experiment Success********************
```

