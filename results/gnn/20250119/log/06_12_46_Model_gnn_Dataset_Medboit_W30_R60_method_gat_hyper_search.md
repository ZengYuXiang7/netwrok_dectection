```python
|2025-01-19 06:12:46| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x793075cea5a0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 60,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 06:12:46| ********************Experiment Start********************
|2025-01-19 06:14:27| Round=1 BestEpoch= 95 Acc=0.7488 F1=0.6808 Precision=0.6903 Recall=0.6767 Training_time=59.4 s 

|2025-01-19 06:14:27| ********************Experiment Results:********************
|2025-01-19 06:14:27| Acc: 0.7488 ± 0.0000
|2025-01-19 06:14:27| F1: 0.6808 ± 0.0000
|2025-01-19 06:14:27| P: 0.6903 ± 0.0000
|2025-01-19 06:14:27| Recall: 0.6767 ± 0.0000
|2025-01-19 06:14:27| train_time: 59.3734 ± 0.0000
|2025-01-19 06:14:29| Flops: 43891200
|2025-01-19 06:14:29| Params: 36488
|2025-01-19 06:14:29| Inference time: 1.43 ms
|2025-01-19 06:14:30| ********************Experiment Success********************
```

