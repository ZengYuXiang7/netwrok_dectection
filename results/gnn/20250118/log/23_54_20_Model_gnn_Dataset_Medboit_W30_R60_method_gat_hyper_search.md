```python
|2025-01-18 23:54:20| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x73c44b2cc140>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 60,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 23:54:20| ********************Experiment Start********************
|2025-01-18 23:57:51| Round=1 BestEpoch= 58 Acc=0.9331 F1=0.7367 Precision=0.7435 Recall=0.7333 Training_time=116.1 s 

|2025-01-18 23:57:51| ********************Experiment Results:********************
|2025-01-18 23:57:51| Acc: 0.9331 ± 0.0000
|2025-01-18 23:57:51| F1: 0.7367 ± 0.0000
|2025-01-18 23:57:51| P: 0.7435 ± 0.0000
|2025-01-18 23:57:51| Recall: 0.7333 ± 0.0000
|2025-01-18 23:57:51| train_time: 116.1299 ± 0.0000
|2025-01-18 23:57:58| Flops: 43891200
|2025-01-18 23:57:58| Params: 36488
|2025-01-18 23:57:58| Inference time: 1.52 ms
|2025-01-18 23:57:58| ********************Experiment Success********************
```

