```python
|2025-01-18 03:24:02| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x7f56749773e0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 60,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 03:24:02| ********************Experiment Start********************
|2025-01-18 04:25:56| Round=1 BestEpoch=189 Acc=0.8371 F1=0.7510 Precision=0.7613 Recall=0.7466 Training_time=2900.8 s 

|2025-01-18 04:25:56| ********************Experiment Results:********************
|2025-01-18 04:25:56| Acc: 0.8371 ± 0.0000
|2025-01-18 04:25:56| F1: 0.7510 ± 0.0000
|2025-01-18 04:25:56| P: 0.7613 ± 0.0000
|2025-01-18 04:25:56| Recall: 0.7466 ± 0.0000
|2025-01-18 04:25:56| train_time: 2900.7936 ± 0.0000
|2025-01-18 04:26:30| Flops: 45388800
|2025-01-18 04:26:30| Params: 59901
|2025-01-18 04:26:30| Inference time: 4.03 ms
|2025-01-18 04:26:31| ********************Experiment Success********************
```

