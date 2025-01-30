```python
|2025-01-19 04:55:02| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x7d695af55d90>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 60,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 04:55:02| ********************Experiment Start********************
|2025-01-19 05:13:43| Round=1 BestEpoch=197 Acc=0.8932 F1=0.8271 Precision=0.8342 Recall=0.8243 Training_time=856.4 s 

|2025-01-19 05:13:43| ********************Experiment Results:********************
|2025-01-19 05:13:43| Acc: 0.8932 ± 0.0000
|2025-01-19 05:13:43| F1: 0.8271 ± 0.0000
|2025-01-19 05:13:43| P: 0.8342 ± 0.0000
|2025-01-19 05:13:43| Recall: 0.8243 ± 0.0000
|2025-01-19 05:13:43| train_time: 856.4092 ± 0.0000
|2025-01-19 05:13:58| Flops: 45388800
|2025-01-19 05:13:58| Params: 59901
|2025-01-19 05:13:58| Inference time: 1.43 ms
|2025-01-19 05:13:58| ********************Experiment Success********************
```

