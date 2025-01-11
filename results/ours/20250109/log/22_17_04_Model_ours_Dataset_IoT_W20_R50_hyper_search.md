```python
|2025-01-09 22:17:04| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x71fa6be7bda0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 22:17:04| ********************Experiment Start********************
|2025-01-09 22:17:06| Acc=0.9027 F1=0.8542 Precision=0.8568 Recall=0.8540 time=355.8 s 
|2025-01-09 22:17:06| ********************Experiment Results:********************
|2025-01-09 22:17:06| Acc: 0.9027 ± 0.0000
|2025-01-09 22:17:06| F1: 0.8542 ± 0.0000
|2025-01-09 22:17:06| P: 0.8568 ± 0.0000
|2025-01-09 22:17:06| Recall: 0.8540 ± 0.0000
|2025-01-09 22:17:06| train_time: 355.8068 ± 0.0000
|2025-01-09 22:17:07| Flops: 21833600
|2025-01-09 22:17:07| Params: 67071
|2025-01-09 22:17:07| Inference time: 0.47 ms
|2025-01-09 22:17:07| ********************Experiment Success********************
```

