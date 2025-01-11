```python
|2025-01-11 06:08:56| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x73f99f2d1e80>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 6, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 06:08:56| ********************Experiment Start********************
|2025-01-11 06:27:59| Round=1 BestEpoch=172 Acc=0.7753 F1=0.6884 Precision=0.7193 Recall=0.6700 Training_time=795.7 s 

|2025-01-11 06:27:59| ********************Experiment Results:********************
|2025-01-11 06:27:59| Acc: 0.7753 ± 0.0000
|2025-01-11 06:27:59| F1: 0.6884 ± 0.0000
|2025-01-11 06:27:59| P: 0.7193 ± 0.0000
|2025-01-11 06:27:59| Recall: 0.6700 ± 0.0000
|2025-01-11 06:27:59| train_time: 795.7146 ± 0.0000
|2025-01-11 06:28:24| Flops: 4864000
|2025-01-11 06:28:24| Params: 23771
|2025-01-11 06:28:24| Inference time: 0.30 ms
|2025-01-11 06:28:25| ********************Experiment Success********************
```

