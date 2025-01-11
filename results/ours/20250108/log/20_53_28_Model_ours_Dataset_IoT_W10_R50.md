```python
|2025-01-08 20:53:28| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0x7a4c9a683c20>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 50, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 20:53:28| ********************Experiment Start********************
|2025-01-08 20:55:56| Round=1 BestEpoch=  1 Acc=0.0425 F1=0.0039 Precision=0.0020 Recall=0.0476 Training_time=4.9 s 

|2025-01-08 20:55:56| ********************Experiment Results:********************
|2025-01-08 20:55:56| Acc: 0.0425 ± 0.0000
|2025-01-08 20:55:56| F1: 0.0039 ± 0.0000
|2025-01-08 20:55:56| P: 0.0020 ± 0.0000
|2025-01-08 20:55:56| Recall: 0.0476 ± 0.0000
|2025-01-08 20:55:56| train_time: 4.8779 ± 0.0000
|2025-01-08 20:56:13| Flops: 97638400
|2025-01-08 20:56:13| Params: 381025
|2025-01-08 20:56:13| Inference time: 0.37 ms
|2025-01-08 20:56:14| ********************Experiment Success********************
```

```python
|2025-01-08 20:56:14| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0x7a4c28f334a0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 80, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 20:56:14| ********************Experiment Start********************
