```python
|2025-01-19 05:47:57| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x76b7b0dcef00>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 05:47:57| ********************Experiment Start********************
|2025-01-19 06:04:45| Round=1 BestEpoch=219 Acc=0.7507 F1=0.6510 Precision=0.7029 Recall=0.6289 Training_time=128.8 s 

|2025-01-19 06:04:45| ********************Experiment Results:********************
|2025-01-19 06:04:45| Acc: 0.7507 ± 0.0000
|2025-01-19 06:04:45| F1: 0.6510 ± 0.0000
|2025-01-19 06:04:45| P: 0.7029 ± 0.0000
|2025-01-19 06:04:45| Recall: 0.6289 ± 0.0000
|2025-01-19 06:04:45| train_time: 128.7970 ± 0.0000
|2025-01-19 06:04:47| Flops: 1612800
|2025-01-19 06:04:47| Params: 9928
|2025-01-19 06:04:47| Inference time: 1.14 ms
|2025-01-19 06:04:47| ********************Experiment Success********************
```

