```python
|2025-01-18 23:32:55| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7f2c0907bdd0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 23:32:55| ********************Experiment Start********************
|2025-01-18 23:38:13| Round=1 BestEpoch=137 Acc=0.9364 F1=0.7268 Precision=0.7267 Recall=0.7284 Training_time=220.1 s 

|2025-01-18 23:38:13| ********************Experiment Results:********************
|2025-01-18 23:38:13| Acc: 0.9364 ± 0.0000
|2025-01-18 23:38:13| F1: 0.7268 ± 0.0000
|2025-01-18 23:38:13| P: 0.7267 ± 0.0000
|2025-01-18 23:38:13| Recall: 0.7284 ± 0.0000
|2025-01-18 23:38:13| train_time: 220.1086 ± 0.0000
|2025-01-18 23:38:20| Flops: 2016000
|2025-01-18 23:38:20| Params: 12408
|2025-01-18 23:38:20| Inference time: 1.29 ms
|2025-01-18 23:38:20| ********************Experiment Success********************
```

