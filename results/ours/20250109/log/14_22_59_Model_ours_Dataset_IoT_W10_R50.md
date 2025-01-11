```python
|2025-01-09 14:22:59| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'log': <utils.logger.Logger object at 0x71acd835baa0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': ours, 'num_classes': 6, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 0,
}
|2025-01-09 14:22:59| ********************Experiment Start********************
|2025-01-09 14:29:13| Round=1 BestEpoch=194 Acc=0.7297 F1=0.6222 Precision=0.6607 Recall=0.6067 Training_time=223.6 s 

|2025-01-09 14:29:13| ********************Experiment Results:********************
|2025-01-09 14:29:13| Acc: 0.7297 ± 0.0000
|2025-01-09 14:29:13| F1: 0.6222 ± 0.0000
|2025-01-09 14:29:13| P: 0.6607 ± 0.0000
|2025-01-09 14:29:13| Recall: 0.6067 ± 0.0000
|2025-01-09 14:29:13| train_time: 223.5998 ± 0.0000
|2025-01-09 14:29:14| Flops: 7788800
|2025-01-09 14:29:14| Params: 30029
|2025-01-09 14:29:14| Inference time: 0.28 ms
|2025-01-09 14:29:14| ********************Experiment Success********************
```

```python
|2025-01-09 14:29:14| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'log': <utils.logger.Logger object at 0x71aae574e840>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': ours, 'num_classes': 6, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 80, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 0,
}
|2025-01-09 14:29:14| ********************Experiment Start********************
|2025-01-09 14:29:17| ********************Experiment Results:********************
|2025-01-09 14:29:19| Flops: 16908800
|2025-01-09 14:29:19| Params: 65429
|2025-01-09 14:29:19| Inference time: 0.28 ms
