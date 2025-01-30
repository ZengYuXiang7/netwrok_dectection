```python
|2025-01-18 23:42:40| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x7ccf5b0f7260>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 40,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 23:42:40| ********************Experiment Start********************
|2025-01-18 23:47:58| Round=1 BestEpoch= 99 Acc=0.9367 F1=0.7382 Precision=0.7470 Recall=0.7309 Training_time=212.1 s 

|2025-01-18 23:47:58| ********************Experiment Results:********************
|2025-01-18 23:47:58| Acc: 0.9367 ± 0.0000
|2025-01-18 23:47:58| F1: 0.7382 ± 0.0000
|2025-01-18 23:47:58| P: 0.7470 ± 0.0000
|2025-01-18 23:47:58| Recall: 0.7309 ± 0.0000
|2025-01-18 23:47:58| train_time: 212.1144 ± 0.0000
|2025-01-18 23:48:05| Flops: 20044800
|2025-01-18 23:48:05| Params: 19528
|2025-01-18 23:48:05| Inference time: 1.49 ms
|2025-01-18 23:48:05| ********************Experiment Success********************
```

