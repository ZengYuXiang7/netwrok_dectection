```python
|2025-01-18 22:55:27| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7f40b07b9fd0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 22:55:27| ********************Experiment Start********************
|2025-01-18 22:56:29| Round=1 BestEpoch=114 Acc=0.9331 F1=0.7223 Precision=0.7296 Recall=0.7188 Training_time=37.4 s 

|2025-01-18 22:56:29| ********************Experiment Results:********************
|2025-01-18 22:56:29| Acc: 0.9331 ± 0.0000
|2025-01-18 22:56:29| F1: 0.7223 ± 0.0000
|2025-01-18 22:56:29| P: 0.7296 ± 0.0000
|2025-01-18 22:56:29| Recall: 0.7188 ± 0.0000
|2025-01-18 22:56:29| train_time: 37.3750 ± 0.0000
|2025-01-18 22:56:29| Flops: 80486400
|2025-01-18 22:56:29| Params: 29608
|2025-01-18 22:56:29| Inference time: 0.07 ms
|2025-01-18 22:56:29| ********************Experiment Success********************
```

