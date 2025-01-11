```python
|2025-01-09 16:55:24| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7f39b92ba510>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': mlp, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 16:55:24| ********************Experiment Start********************
|2025-01-09 16:55:25| Acc=0.7605 F1=0.6520 Precision=0.6744 Recall=0.6413 time=1.2 s 
|2025-01-09 16:55:25| ********************Experiment Results:********************
|2025-01-09 16:55:25| Acc: 0.7605 ± 0.0000
|2025-01-09 16:55:25| F1: 0.6520 ± 0.0000
|2025-01-09 16:55:25| P: 0.6744 ± 0.0000
|2025-01-09 16:55:25| Recall: 0.6413 ± 0.0000
|2025-01-09 16:55:25| train_time: 1.1500 ± 0.0000
|2025-01-09 16:55:26| Flops: 644352
|2025-01-09 16:55:26| Params: 4913
|2025-01-09 16:55:26| Inference time: 0.10 ms
|2025-01-09 16:55:26| ********************Experiment Success********************
```

