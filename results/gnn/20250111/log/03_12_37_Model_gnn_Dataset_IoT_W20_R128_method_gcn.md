```python
|2025-01-11 03:12:37| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xcf8c9f5ecc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 6, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 03:12:37| ********************Experiment Start********************
|2025-01-11 03:12:56| Acc=0.8406 F1=0.7662 Precision=0.7777 Recall=0.7580 time=2194.0 s 
|2025-01-11 03:12:56| ********************Experiment Results:********************
|2025-01-11 03:12:56| Acc: 0.8406 ± 0.0000
|2025-01-11 03:12:56| F1: 0.7662 ± 0.0000
|2025-01-11 03:12:56| P: 0.7777 ± 0.0000
|2025-01-11 03:12:56| Recall: 0.7580 ± 0.0000
|2025-01-11 03:12:56| train_time: 2193.9564 ± 0.0000
|2025-01-11 03:13:19| Flops: 5570560
|2025-01-11 03:13:19| Params: 54805
|2025-01-11 03:13:19| Inference time: 1.44 ms
|2025-01-11 03:13:19| ********************Experiment Success********************
```

