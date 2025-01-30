```python
|2025-01-18 23:58:01| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0xb6250bd3b30>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 23:58:01| ********************Experiment Start********************
|2025-01-18 23:58:07| Acc=0.9372 F1=0.7343 Precision=0.7503 Recall=0.7199 time=253.5 s 
|2025-01-18 23:58:07| ********************Experiment Results:********************
|2025-01-18 23:58:07| Acc: 0.9372 ± 0.0000
|2025-01-18 23:58:07| F1: 0.7343 ± 0.0000
|2025-01-18 23:58:07| P: 0.7503 ± 0.0000
|2025-01-18 23:58:07| Recall: 0.7199 ± 0.0000
|2025-01-18 23:58:07| train_time: 253.4791 ± 0.0000
|2025-01-18 23:58:15| Flops: 30816000
|2025-01-18 23:58:15| Params: 27408
|2025-01-18 23:58:15| Inference time: 1.81 ms
|2025-01-18 23:58:15| ********************Experiment Success********************
```

