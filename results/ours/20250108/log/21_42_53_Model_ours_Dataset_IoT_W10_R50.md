```python
|2025-01-08 21:42:53| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0x1269e4566210>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 50, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 21:42:53| ********************Experiment Start********************
|2025-01-08 21:42:58| Acc=0.6072 F1=0.5367 Precision=0.5994 Recall=0.5170
|2025-01-08 21:42:58| ********************Experiment Results:********************
|2025-01-08 21:42:58| Acc: 0.6072 ± 0.0000
|2025-01-08 21:42:58| F1: 0.5367 ± 0.0000
|2025-01-08 21:42:58| P: 0.5994 ± 0.0000
|2025-01-08 21:42:58| Recall: 0.5170 ± 0.0000
|2025-01-08 21:42:58| train_time: 526.2753 ± 0.0000
|2025-01-08 21:43:01| Flops: 106860800
|2025-01-08 21:43:01| Params: 417029
|2025-01-08 21:43:01| Inference time: 0.35 ms
|2025-01-08 21:43:01| ********************Experiment Success********************
```

