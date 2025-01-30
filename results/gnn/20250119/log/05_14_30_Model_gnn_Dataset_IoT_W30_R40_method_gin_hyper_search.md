```python
|2025-01-19 05:14:30| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gin, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x753f6cf56f00>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 05:14:30| ********************Experiment Start********************
|2025-01-19 05:25:42| Round=1 BestEpoch=243 Acc=0.8232 F1=0.7373 Precision=0.7601 Recall=0.7290 Training_time=487.9 s 

|2025-01-19 05:25:42| ********************Experiment Results:********************
|2025-01-19 05:25:42| Acc: 0.8232 ± 0.0000
|2025-01-19 05:25:42| F1: 0.7373 ± 0.0000
|2025-01-19 05:25:42| P: 0.7601 ± 0.0000
|2025-01-19 05:25:42| Recall: 0.7290 ± 0.0000
|2025-01-19 05:25:42| train_time: 487.9451 ± 0.0000
|2025-01-19 05:25:57| Flops: 5068800
|2025-01-19 05:25:57| Params: 27021
|2025-01-19 05:25:57| Inference time: 0.29 ms
|2025-01-19 05:25:58| ********************Experiment Success********************
```

