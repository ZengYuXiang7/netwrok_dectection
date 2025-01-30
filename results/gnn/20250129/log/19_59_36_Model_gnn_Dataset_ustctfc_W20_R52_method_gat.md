```python
|2025-01-29 19:59:36| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0x8beb8dd2810>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 19:59:36| ********************Experiment Start********************
|2025-01-29 19:59:58| Round=1 BestEpoch= 29 Ac=0.8450 Pr=0.7635 Rc=0.6838 F1=0.7031 Training_time=6.8 s 

|2025-01-29 19:59:58| ********************Experiment Results:********************
|2025-01-29 19:59:58| AC: 0.8450 ± 0.0000
|2025-01-29 19:59:58| PR: 0.7635 ± 0.0000
|2025-01-29 19:59:58| RC: 0.6838 ± 0.0000
|2025-01-29 19:59:58| F1: 0.7031 ± 0.0000
|2025-01-29 19:59:58| train_time: 6.8331 ± 0.0000
|2025-01-29 19:59:59| Flops: 22763520
|2025-01-29 19:59:59| Params: 34337
|2025-01-29 19:59:59| Inference time: 1.54 ms
|2025-01-29 19:59:59| ********************Experiment Success********************
```

