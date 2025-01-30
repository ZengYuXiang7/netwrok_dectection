```python
|2025-01-18 23:02:51| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x76e432f36cc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 23:02:51| ********************Experiment Start********************
|2025-01-18 23:12:28| Round=1 BestEpoch=204 Acc=0.9377 F1=0.7367 Precision=0.7489 Recall=0.7258 Training_time=325.0 s 

|2025-01-18 23:12:28| ********************Experiment Results:********************
|2025-01-18 23:12:28| Acc: 0.9377 ± 0.0000
|2025-01-18 23:12:28| F1: 0.7367 ± 0.0000
|2025-01-18 23:12:28| P: 0.7489 ± 0.0000
|2025-01-18 23:12:28| Recall: 0.7258 ± 0.0000
|2025-01-18 23:12:28| train_time: 324.9839 ± 0.0000
|2025-01-18 23:12:35| Flops: 1612800
|2025-01-18 23:12:35| Params: 9928
|2025-01-18 23:12:35| Inference time: 1.26 ms
|2025-01-18 23:12:35| ********************Experiment Success********************
```

