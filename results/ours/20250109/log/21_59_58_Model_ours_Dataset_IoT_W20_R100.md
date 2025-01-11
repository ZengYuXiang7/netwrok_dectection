```python
|2025-01-09 21:59:58| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': False, 'log': <utils.logger.Logger object at 0xc55f1307140>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 100,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 21:59:58| ********************Experiment Start********************
|2025-01-09 21:59:59| Acc=0.8385 F1=0.7856 Precision=0.7883 Recall=0.7899 time=53.2 s 
|2025-01-09 21:59:59| ********************Experiment Results:********************
|2025-01-09 21:59:59| Acc: 0.8385 ± 0.0000
|2025-01-09 21:59:59| F1: 0.7856 ± 0.0000
|2025-01-09 21:59:59| P: 0.7883 ± 0.0000
|2025-01-09 21:59:59| Recall: 0.7899 ± 0.0000
|2025-01-09 21:59:59| train_time: 53.1748 ± 0.0000
|2025-01-09 22:00:00| Flops: 503123200
|2025-01-09 22:00:00| Params: 423421
|2025-01-09 22:00:00| Inference time: 0.44 ms
|2025-01-09 22:00:00| ********************Experiment Success********************
```

