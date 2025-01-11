```python
|2025-01-11 04:54:33| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x7e0125d96c60>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 6, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 100,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 04:54:33| ********************Experiment Start********************
|2025-01-11 05:32:29| Round=1 BestEpoch=211 Acc=0.8845 F1=0.8188 Precision=0.8246 Recall=0.8151 Training_time=1780.6 s 

|2025-01-11 05:32:29| ********************Experiment Results:********************
|2025-01-11 05:32:29| Acc: 0.8845 ± 0.0000
|2025-01-11 05:32:29| F1: 0.8188 ± 0.0000
|2025-01-11 05:32:29| P: 0.8246 ± 0.0000
|2025-01-11 05:32:29| Recall: 0.8151 ± 0.0000
|2025-01-11 05:32:29| train_time: 1780.6152 ± 0.0000
|2025-01-11 05:32:54| Flops: 81152000
|2025-01-11 05:32:54| Params: 102821
|2025-01-11 05:32:54| Inference time: 1.58 ms
|2025-01-11 05:32:55| ********************Experiment Success********************
```

