```python
|2025-01-19 06:05:51| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7edbbed10bc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 60, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 06:05:51| ********************Experiment Start********************
|2025-01-19 06:07:48| Round=1 BestEpoch=153 Acc=0.7607 F1=0.6983 Precision=0.7096 Recall=0.6888 Training_time=73.6 s 

|2025-01-19 06:07:48| ********************Experiment Results:********************
|2025-01-19 06:07:48| Acc: 0.7607 ± 0.0000
|2025-01-19 06:07:48| F1: 0.6983 ± 0.0000
|2025-01-19 06:07:48| P: 0.7096 ± 0.0000
|2025-01-19 06:07:48| Recall: 0.6888 ± 0.0000
|2025-01-19 06:07:48| train_time: 73.6370 ± 0.0000
|2025-01-19 06:07:50| Flops: 2419200
|2025-01-19 06:07:50| Params: 14888
|2025-01-19 06:07:50| Inference time: 1.18 ms
|2025-01-19 06:07:50| ********************Experiment Success********************
```

