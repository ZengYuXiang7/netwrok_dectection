```python
|2025-01-19 06:20:20| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x1179dbc28740>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 06:20:20| ********************Experiment Start********************
|2025-01-19 06:20:22| Acc=0.7339 F1=0.6783 Precision=0.6891 Recall=0.6695 time=64.3 s 
|2025-01-19 06:20:22| ********************Experiment Results:********************
|2025-01-19 06:20:22| Acc: 0.7339 ± 0.0000
|2025-01-19 06:20:22| F1: 0.6783 ± 0.0000
|2025-01-19 06:20:22| P: 0.6891 ± 0.0000
|2025-01-19 06:20:22| Recall: 0.6695 ± 0.0000
|2025-01-19 06:20:22| train_time: 64.2652 ± 0.0000
|2025-01-19 06:20:24| Flops: 4070400
|2025-01-19 06:20:24| Params: 11408
|2025-01-19 06:20:24| Inference time: 0.32 ms
|2025-01-19 06:20:24| ********************Experiment Success********************
```

