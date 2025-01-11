```python
|2025-01-08 15:35:17| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0x72d7311fee40>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 50, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 15:35:17| ********************Experiment Start********************
|2025-01-08 15:46:55| Round=1 BestEpoch=179 Acc=0.6057 F1=0.5368 Precision=0.5977 Recall=0.5182 Training_time=508.3 s 

|2025-01-08 15:46:55| ********************Experiment Results:********************
|2025-01-08 15:46:55| Acc: 0.6057 ± 0.0000
|2025-01-08 15:46:55| F1: 0.5368 ± 0.0000
|2025-01-08 15:46:55| P: 0.5977 ± 0.0000
|2025-01-08 15:46:55| Recall: 0.5182 ± 0.0000
|2025-01-08 15:46:55| train_time: 508.3164 ± 0.0000
|2025-01-08 15:46:59| Flops: 17928704
|2025-01-08 15:46:59| Params: 69913
|2025-01-08 15:46:59| Inference time: 0.06 ms
|2025-01-08 15:46:59| ********************Experiment Success********************
```

```python
|2025-01-08 15:46:59| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0x72d501fd6630>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 80, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 15:46:59| ********************Experiment Start********************
|2025-01-08 15:55:35| Round=1 BestEpoch=106 Acc=0.6340 F1=0.5754 Precision=0.6490 Recall=0.5474 Training_time=312.0 s 

|2025-01-08 15:55:35| ********************Experiment Results:********************
|2025-01-08 15:55:35| Acc: 0.6340 ± 0.0000
|2025-01-08 15:55:35| F1: 0.5754 ± 0.0000
|2025-01-08 15:55:35| P: 0.6490 ± 0.0000
|2025-01-08 15:55:35| Recall: 0.5474 ± 0.0000
|2025-01-08 15:55:35| train_time: 312.0211 ± 0.0000
|2025-01-08 15:55:38| Flops: 29287424
|2025-01-08 15:55:38| Params: 114223
|2025-01-08 15:55:38| Inference time: 0.06 ms
|2025-01-08 15:55:39| ********************Experiment Success********************
```

```python
|2025-01-08 15:55:39| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0x72d6bc916f30>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 100, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 15:55:39| ********************Experiment Start********************
|2025-01-08 16:04:43| Round=1 BestEpoch=106 Acc=0.6451 F1=0.5898 Precision=0.6580 Recall=0.5609 Training_time=332.1 s 

|2025-01-08 16:04:43| ********************Experiment Results:********************
|2025-01-08 16:04:43| Acc: 0.6451 ± 0.0000
|2025-01-08 16:04:43| F1: 0.5898 ± 0.0000
|2025-01-08 16:04:43| P: 0.6580 ± 0.0000
|2025-01-08 16:04:43| Recall: 0.5609 ± 0.0000
|2025-01-08 16:04:43| train_time: 332.1187 ± 0.0000
|2025-01-08 16:04:46| Flops: 37115904
|2025-01-08 16:04:46| Params: 144763
|2025-01-08 16:04:46| Inference time: 0.08 ms
|2025-01-08 16:04:47| ********************Experiment Success********************
```

```python
|2025-01-08 16:04:47| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0x72d6bdd9daf0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 50, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 16:04:47| ********************Experiment Start********************
|2025-01-08 16:05:38| ********************Experiment Results:********************
|2025-01-08 16:05:57| Flops: 75942400
|2025-01-08 16:05:57| Params: 295871
|2025-01-08 16:05:57| Inference time: 0.10 ms
