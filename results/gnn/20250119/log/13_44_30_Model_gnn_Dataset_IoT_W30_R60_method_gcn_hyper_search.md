```python
|2025-01-19 13:44:30| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x733198191340>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 60, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 13:44:30| ********************Experiment Start********************
|2025-01-19 14:02:40| Round=1 BestEpoch=259 Acc=0.8736 F1=0.8053 Precision=0.8102 Recall=0.8032 Training_time=833.0 s 

|2025-01-19 14:02:40| ********************Experiment Results:********************
|2025-01-19 14:02:40| Acc: 0.8736 ± 0.0000
|2025-01-19 14:02:40| F1: 0.8053 ± 0.0000
|2025-01-19 14:02:40| P: 0.8102 ± 0.0000
|2025-01-19 14:02:40| Recall: 0.8032 ± 0.0000
|2025-01-19 14:02:40| train_time: 832.9700 ± 0.0000
|2025-01-19 14:02:55| Flops: 3916800
|2025-01-19 14:02:55| Params: 38301
|2025-01-19 14:02:55| Inference time: 1.20 ms
|2025-01-19 14:02:55| ********************Experiment Success********************
```

