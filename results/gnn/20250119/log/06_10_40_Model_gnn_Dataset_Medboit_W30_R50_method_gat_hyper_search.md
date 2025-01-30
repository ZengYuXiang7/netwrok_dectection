```python
|2025-01-19 06:10:40| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x73c5332c73b0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 06:10:40| ********************Experiment Start********************
|2025-01-19 06:12:41| Round=1 BestEpoch=124 Acc=0.7517 F1=0.6924 Precision=0.6993 Recall=0.6878 Training_time=77.6 s 

|2025-01-19 06:12:41| ********************Experiment Results:********************
|2025-01-19 06:12:41| Acc: 0.7517 ± 0.0000
|2025-01-19 06:12:41| F1: 0.6924 ± 0.0000
|2025-01-19 06:12:41| P: 0.6993 ± 0.0000
|2025-01-19 06:12:41| Recall: 0.6878 ± 0.0000
|2025-01-19 06:12:41| train_time: 77.5583 ± 0.0000
|2025-01-19 06:12:43| Flops: 30816000
|2025-01-19 06:12:43| Params: 27408
|2025-01-19 06:12:43| Inference time: 1.46 ms
|2025-01-19 06:12:44| ********************Experiment Success********************
```

