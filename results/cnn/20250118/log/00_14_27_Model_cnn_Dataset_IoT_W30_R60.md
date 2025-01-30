```python
|2025-01-18 00:14:27| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xd5b9d3d3140>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 00:14:27| ********************Experiment Start********************
|2025-01-18 00:14:28| Acc=0.8393 F1=0.7521 Precision=0.7899 Recall=0.7440 time=169.2 s 
|2025-01-18 00:14:28| ********************Experiment Results:********************
|2025-01-18 00:14:28| Acc: 0.8393 ± 0.0000
|2025-01-18 00:14:28| F1: 0.7521 ± 0.0000
|2025-01-18 00:14:28| P: 0.7899 ± 0.0000
|2025-01-18 00:14:28| Recall: 0.7440 ± 0.0000
|2025-01-18 00:14:28| train_time: 169.2033 ± 0.0000
|2025-01-18 00:14:28| Flops: 44405760
|2025-01-18 00:14:28| Params: 12621
|2025-01-18 00:14:28| Inference time: 0.11 ms
|2025-01-18 00:14:28| ********************Experiment Success********************
```

