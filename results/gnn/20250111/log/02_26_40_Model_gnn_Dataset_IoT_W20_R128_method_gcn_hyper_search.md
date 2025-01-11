```python
|2025-01-11 02:26:40| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x73806ae4d3d0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 6, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 02:26:40| ********************Experiment Start********************
|2025-01-11 03:12:09| Round=1 BestEpoch=351 Acc=0.8599 F1=0.7921 Precision=0.8013 Recall=0.7853 Training_time=2194.0 s 

|2025-01-11 03:12:09| ********************Experiment Results:********************
|2025-01-11 03:12:09| Acc: 0.8599 ± 0.0000
|2025-01-11 03:12:09| F1: 0.7921 ± 0.0000
|2025-01-11 03:12:09| P: 0.8013 ± 0.0000
|2025-01-11 03:12:09| Recall: 0.7853 ± 0.0000
|2025-01-11 03:12:09| train_time: 2193.9564 ± 0.0000
|2025-01-11 03:12:34| Flops: 5570560
|2025-01-11 03:12:34| Params: 54805
|2025-01-11 03:12:34| Inference time: 1.24 ms
|2025-01-11 03:12:34| ********************Experiment Success********************
```

