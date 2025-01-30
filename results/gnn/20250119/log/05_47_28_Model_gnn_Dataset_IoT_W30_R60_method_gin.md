```python
|2025-01-19 05:47:28| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x115abc4e9c40>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 60, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 05:47:28| ********************Experiment Start********************
|2025-01-19 05:47:40| Acc=0.8193 F1=0.7311 Precision=0.7410 Recall=0.7267 time=495.1 s 
|2025-01-19 05:47:40| ********************Experiment Results:********************
|2025-01-19 05:47:40| Acc: 0.8193 ± 0.0000
|2025-01-19 05:47:40| F1: 0.7311 ± 0.0000
|2025-01-19 05:47:40| P: 0.7410 ± 0.0000
|2025-01-19 05:47:40| Recall: 0.7267 ± 0.0000
|2025-01-19 05:47:40| train_time: 495.0858 ± 0.0000
|2025-01-19 05:47:55| Flops: 9907200
|2025-01-19 05:47:55| Params: 41721
|2025-01-19 05:47:55| Inference time: 0.33 ms
|2025-01-19 05:47:55| ********************Experiment Success********************
```

