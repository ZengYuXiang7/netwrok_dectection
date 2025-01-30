```python
|2025-01-19 14:35:59| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x7b1fb3a96300>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 14:35:59| ********************Experiment Start********************
|2025-01-19 14:54:49| Round=1 BestEpoch=186 Acc=0.8813 F1=0.8121 Precision=0.8177 Recall=0.8105 Training_time=859.1 s 

|2025-01-19 14:54:49| ********************Experiment Results:********************
|2025-01-19 14:54:49| Acc: 0.8813 ± 0.0000
|2025-01-19 14:54:49| F1: 0.8121 ± 0.0000
|2025-01-19 14:54:49| P: 0.8177 ± 0.0000
|2025-01-19 14:54:49| Recall: 0.8105 ± 0.0000
|2025-01-19 14:54:49| train_time: 859.1187 ± 0.0000
|2025-01-19 14:55:04| Flops: 32064000
|2025-01-19 14:55:04| Params: 46921
|2025-01-19 14:55:04| Inference time: 1.50 ms
|2025-01-19 14:55:05| ********************Experiment Success********************
```

