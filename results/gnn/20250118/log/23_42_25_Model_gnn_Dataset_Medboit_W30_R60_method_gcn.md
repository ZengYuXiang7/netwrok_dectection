```python
|2025-01-18 23:42:25| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x97b84b688c0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 60, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 23:42:25| ********************Experiment Start********************
|2025-01-18 23:42:31| Acc=0.9318 F1=0.7037 Precision=0.7184 Recall=0.6910 time=146.0 s 
|2025-01-18 23:42:31| ********************Experiment Results:********************
|2025-01-18 23:42:31| Acc: 0.9318 ± 0.0000
|2025-01-18 23:42:31| F1: 0.7037 ± 0.0000
|2025-01-18 23:42:31| P: 0.7184 ± 0.0000
|2025-01-18 23:42:31| Recall: 0.6910 ± 0.0000
|2025-01-18 23:42:31| train_time: 146.0490 ± 0.0000
|2025-01-18 23:42:38| Flops: 2419200
|2025-01-18 23:42:38| Params: 14888
|2025-01-18 23:42:38| Inference time: 1.37 ms
|2025-01-18 23:42:38| ********************Experiment Success********************
```

