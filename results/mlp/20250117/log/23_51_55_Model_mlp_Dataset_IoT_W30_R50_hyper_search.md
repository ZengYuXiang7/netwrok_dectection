```python
|2025-01-17 23:51:55| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7aec485ca3f0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-17 23:51:55| ********************Experiment Start********************
|2025-01-17 23:54:18| Round=1 BestEpoch=190 Acc=0.7417 F1=0.6330 Precision=0.6441 Recall=0.6306 Training_time=99.5 s 

|2025-01-17 23:54:18| ********************Experiment Results:********************
|2025-01-17 23:54:18| Acc: 0.7417 ± 0.0000
|2025-01-17 23:54:18| F1: 0.6330 ± 0.0000
|2025-01-17 23:54:18| P: 0.6441 ± 0.0000
|2025-01-17 23:54:18| Recall: 0.6306 ± 0.0000
|2025-01-17 23:54:18| train_time: 99.4612 ± 0.0000
|2025-01-17 23:54:18| Flops: 708352
|2025-01-17 23:54:18| Params: 5413
|2025-01-17 23:54:18| Inference time: 0.05 ms
|2025-01-17 23:54:18| ********************Experiment Success********************
```

