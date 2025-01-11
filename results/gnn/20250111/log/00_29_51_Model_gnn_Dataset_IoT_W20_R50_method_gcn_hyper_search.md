```python
|2025-01-11 00:29:51| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x73e0e50933e0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 6, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 00:29:51| ********************Experiment Start********************
|2025-01-11 01:03:32| Round=1 BestEpoch=251 Acc=0.8144 F1=0.7400 Precision=0.7666 Recall=0.7245 Training_time=1576.4 s 

|2025-01-11 01:03:32| ********************Experiment Results:********************
|2025-01-11 01:03:32| Acc: 0.8144 ± 0.0000
|2025-01-11 01:03:32| F1: 0.7400 ± 0.0000
|2025-01-11 01:03:32| P: 0.7666 ± 0.0000
|2025-01-11 01:03:32| Recall: 0.7245 ± 0.0000
|2025-01-11 01:03:32| train_time: 1576.3957 ± 0.0000
|2025-01-11 01:03:56| Flops: 2176000
|2025-01-11 01:03:56| Params: 21421
|2025-01-11 01:03:56| Inference time: 1.25 ms
|2025-01-11 01:03:57| ********************Experiment Success********************
```

