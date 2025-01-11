```python
|2025-01-11 03:13:22| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x72386279c1d0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 6, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 03:13:22| ********************Experiment Start********************
|2025-01-11 04:00:44| Round=1 BestEpoch=277 Acc=0.8661 F1=0.7971 Precision=0.8087 Recall=0.7913 Training_time=2288.9 s 

|2025-01-11 04:00:44| ********************Experiment Results:********************
|2025-01-11 04:00:44| Acc: 0.8661 ± 0.0000
|2025-01-11 04:00:44| F1: 0.7971 ± 0.0000
|2025-01-11 04:00:44| P: 0.8087 ± 0.0000
|2025-01-11 04:00:44| Recall: 0.7913 ± 0.0000
|2025-01-11 04:00:44| train_time: 2288.8550 ± 0.0000
|2025-01-11 04:01:09| Flops: 21376000
|2025-01-11 04:01:09| Params: 36421
|2025-01-11 04:01:09| Inference time: 1.51 ms
|2025-01-11 04:01:10| ********************Experiment Success********************
```

