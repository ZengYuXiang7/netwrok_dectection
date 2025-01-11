```python
|2025-01-09 17:05:48| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x749087526840>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': mlp, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 17:05:48| ********************Experiment Start********************
|2025-01-09 17:05:49| Acc=0.7667 F1=0.6609 Precision=0.6765 Recall=0.6544 time=99.4 s 
|2025-01-09 17:05:49| ********************Experiment Results:********************
|2025-01-09 17:05:49| Acc: 0.7667 ± 0.0000
|2025-01-09 17:05:49| F1: 0.6609 ± 0.0000
|2025-01-09 17:05:49| P: 0.6765 ± 0.0000
|2025-01-09 17:05:49| Recall: 0.6544 ± 0.0000
|2025-01-09 17:05:49| train_time: 99.3835 ± 0.0000
|2025-01-09 17:05:50| Flops: 644352
|2025-01-09 17:05:50| Params: 4913
|2025-01-09 17:05:50| Inference time: 0.07 ms
|2025-01-09 17:05:50| ********************Experiment Success********************
```

