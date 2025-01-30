```python
|2025-01-19 06:07:52| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x12ec003eb8f0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 60, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 06:07:52| ********************Experiment Start********************
|2025-01-19 06:07:54| Acc=0.7527 F1=0.6785 Precision=0.6997 Recall=0.6637 time=73.6 s 
|2025-01-19 06:07:54| ********************Experiment Results:********************
|2025-01-19 06:07:54| Acc: 0.7527 ± 0.0000
|2025-01-19 06:07:54| F1: 0.6785 ± 0.0000
|2025-01-19 06:07:54| P: 0.6997 ± 0.0000
|2025-01-19 06:07:54| Recall: 0.6637 ± 0.0000
|2025-01-19 06:07:54| train_time: 73.6370 ± 0.0000
|2025-01-19 06:07:56| Flops: 2419200
|2025-01-19 06:07:56| Params: 14888
|2025-01-19 06:07:56| Inference time: 1.30 ms
|2025-01-19 06:07:56| ********************Experiment Success********************
```

