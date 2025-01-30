```python
|2025-01-19 05:14:01| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0xe4efe301700>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 60,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 05:14:01| ********************Experiment Start********************
|2025-01-19 05:14:13| Acc=0.8811 F1=0.8175 Precision=0.8280 Recall=0.8118 time=856.4 s 
|2025-01-19 05:14:13| ********************Experiment Results:********************
|2025-01-19 05:14:13| Acc: 0.8811 ± 0.0000
|2025-01-19 05:14:13| F1: 0.8175 ± 0.0000
|2025-01-19 05:14:13| P: 0.8280 ± 0.0000
|2025-01-19 05:14:13| Recall: 0.8118 ± 0.0000
|2025-01-19 05:14:13| train_time: 856.4092 ± 0.0000
|2025-01-19 05:14:28| Flops: 45388800
|2025-01-19 05:14:28| Params: 59901
|2025-01-19 05:14:28| Inference time: 1.67 ms
|2025-01-19 05:14:28| ********************Experiment Success********************
```

