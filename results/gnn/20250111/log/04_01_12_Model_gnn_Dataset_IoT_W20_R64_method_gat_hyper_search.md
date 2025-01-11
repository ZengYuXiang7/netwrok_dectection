```python
|2025-01-11 04:01:12| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x7fa778912660>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 6, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 04:01:12| ********************Experiment Start********************
|2025-01-11 04:54:05| Round=1 BestEpoch=311 Acc=0.8710 F1=0.7995 Precision=0.8095 Recall=0.7936 Training_time=2585.5 s 

|2025-01-11 04:54:05| ********************Experiment Results:********************
|2025-01-11 04:54:05| Acc: 0.8710 ± 0.0000
|2025-01-11 04:54:05| F1: 0.7995 ± 0.0000
|2025-01-11 04:54:05| P: 0.8095 ± 0.0000
|2025-01-11 04:54:05| Recall: 0.7936 ± 0.0000
|2025-01-11 04:54:05| train_time: 2585.4974 ± 0.0000
|2025-01-11 04:54:30| Flops: 34242560
|2025-01-11 04:54:30| Params: 51989
|2025-01-11 04:54:30| Inference time: 1.55 ms
|2025-01-11 04:54:31| ********************Experiment Success********************
```

