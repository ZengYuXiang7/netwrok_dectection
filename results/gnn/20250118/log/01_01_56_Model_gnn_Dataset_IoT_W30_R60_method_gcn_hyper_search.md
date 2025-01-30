```python
|2025-01-18 01:01:56| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7158213ec5c0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 60, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 01:01:56| ********************Experiment Start********************
|2025-01-18 01:47:19| Round=1 BestEpoch=196 Acc=0.8149 F1=0.7272 Precision=0.7456 Recall=0.7179 Training_time=2053.7 s 

|2025-01-18 01:47:19| ********************Experiment Results:********************
|2025-01-18 01:47:19| Acc: 0.8149 ± 0.0000
|2025-01-18 01:47:19| F1: 0.7272 ± 0.0000
|2025-01-18 01:47:19| P: 0.7456 ± 0.0000
|2025-01-18 01:47:19| Recall: 0.7179 ± 0.0000
|2025-01-18 01:47:19| train_time: 2053.6764 ± 0.0000
|2025-01-18 01:47:54| Flops: 3916800
|2025-01-18 01:47:54| Params: 38301
|2025-01-18 01:47:54| Inference time: 3.14 ms
|2025-01-18 01:47:56| ********************Experiment Success********************
```

