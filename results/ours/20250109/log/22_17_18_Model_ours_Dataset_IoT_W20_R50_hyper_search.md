```python
|2025-01-09 22:17:18| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7dfc2d1c8410>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 22:17:18| ********************Experiment Start********************
|2025-01-09 22:17:20| Acc=0.3174 F1=0.3152 Precision=0.3845 Recall=0.3913 time=355.8 s 
|2025-01-09 22:17:20| ********************Experiment Results:********************
|2025-01-09 22:17:20| Acc: 0.3174 ± 0.0000
|2025-01-09 22:17:20| F1: 0.3152 ± 0.0000
|2025-01-09 22:17:20| P: 0.3845 ± 0.0000
|2025-01-09 22:17:20| Recall: 0.3913 ± 0.0000
|2025-01-09 22:17:20| train_time: 355.8068 ± 0.0000
|2025-01-09 22:17:21| Flops: 21833600
|2025-01-09 22:17:21| Params: 67071
|2025-01-09 22:17:21| Inference time: 0.82 ms
|2025-01-09 22:17:21| ********************Experiment Success********************
```

