```python
|2025-01-19 04:05:50| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x7632d21c4980>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 40,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 04:05:50| ********************Experiment Start********************
|2025-01-19 04:36:29| Round=1 BestEpoch=344 Acc=0.8880 F1=0.8170 Precision=0.8226 Recall=0.8148 Training_time=1483.6 s 

|2025-01-19 04:36:29| ********************Experiment Results:********************
|2025-01-19 04:36:29| Acc: 0.8880 ± 0.0000
|2025-01-19 04:36:29| F1: 0.8170 ± 0.0000
|2025-01-19 04:36:29| P: 0.8226 ± 0.0000
|2025-01-19 04:36:29| Recall: 0.8148 ± 0.0000
|2025-01-19 04:36:29| train_time: 1483.6412 ± 0.0000
|2025-01-19 04:36:43| Flops: 21043200
|2025-01-19 04:36:43| Params: 35141
|2025-01-19 04:36:43| Inference time: 1.42 ms
|2025-01-19 04:36:44| ********************Experiment Success********************
```

