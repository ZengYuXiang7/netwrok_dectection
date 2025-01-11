```python
|2025-01-09 14:34:29| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 300, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'log': <utils.logger.Logger object at 0x716059256cc0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': lstm, 'num_classes': 6, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-09 14:34:29| ********************Experiment Start********************
|2025-01-09 14:34:31| Acc=0.6743 F1=0.5474 Precision=0.5659 Recall=0.5392
|2025-01-09 14:34:31| ********************Experiment Results:********************
|2025-01-09 14:34:31| Acc: 0.6743 ± 0.0000
|2025-01-09 14:34:31| F1: 0.5474 ± 0.0000
|2025-01-09 14:34:31| P: 0.5659 ± 0.0000
|2025-01-09 14:34:31| Recall: 0.5392 ± 0.0000
|2025-01-09 14:34:31| train_time: 112.3725 ± 0.0000
|2025-01-09 14:34:32| Flops: 9894400
|2025-01-09 14:34:32| Params: 37871
|2025-01-09 14:34:32| Inference time: 0.08 ms
|2025-01-09 14:34:32| ********************Experiment Success********************
```

```python
|2025-01-09 14:34:32| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 300, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'log': <utils.logger.Logger object at 0x71605562bb60>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': lstm, 'num_classes': 6, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 80, 'record': False,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-09 14:34:32| ********************Experiment Start********************
|2025-01-09 14:34:54| ********************Experiment Results:********************
|2025-01-09 14:34:56| Flops: 23203840
|2025-01-09 14:34:56| Params: 89381
|2025-01-09 14:34:56| Inference time: 0.07 ms
|2025-01-09 14:34:56| ********************Experiment Success********************
```

```python
|2025-01-09 14:34:56| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 300, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'log': <utils.logger.Logger object at 0x7160556f3fb0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': lstm, 'num_classes': 6, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 100, 'record': False,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-09 14:34:56| ********************Experiment Start********************
|2025-01-09 14:42:02| Round=1 BestEpoch=274 Acc=0.7835 F1=0.6961 Precision=0.7365 Recall=0.6849 Training_time=310.9 s 

|2025-01-09 14:42:02| ********************Experiment Results:********************
|2025-01-09 14:42:02| Acc: 0.7835 ± 0.0000
|2025-01-09 14:42:02| F1: 0.6961 ± 0.0000
|2025-01-09 14:42:02| P: 0.7365 ± 0.0000
|2025-01-09 14:42:02| Recall: 0.6849 ± 0.0000
|2025-01-09 14:42:02| train_time: 310.8519 ± 0.0000
|2025-01-09 14:42:03| Flops: 35148800
|2025-01-09 14:42:03| Params: 135721
|2025-01-09 14:42:03| Inference time: 0.09 ms
|2025-01-09 14:42:03| ********************Experiment Success********************
```

```python
|2025-01-09 14:42:03| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'log': <utils.logger.Logger object at 0x71605764ec90>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': cnn, 'num_classes': 6, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 0,
}
|2025-01-09 14:42:03| ********************Experiment Start********************
