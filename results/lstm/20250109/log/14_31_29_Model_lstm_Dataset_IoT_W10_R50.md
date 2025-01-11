```python
|2025-01-09 14:31:29| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'log': <utils.logger.Logger object at 0x769e09f6e150>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': lstm, 'num_classes': 6, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-09 14:31:29| ********************Experiment Start********************
|2025-01-09 14:34:02| Round=1 BestEpoch=195 Acc=0.7247 F1=0.6113 Precision=0.6829 Recall=0.6002 Training_time=112.4 s 

|2025-01-09 14:34:02| ********************Experiment Results:********************
|2025-01-09 14:34:02| Acc: 0.7247 ± 0.0000
|2025-01-09 14:34:02| F1: 0.6113 ± 0.0000
|2025-01-09 14:34:02| P: 0.6829 ± 0.0000
|2025-01-09 14:34:02| Recall: 0.6002 ± 0.0000
|2025-01-09 14:34:02| train_time: 112.3725 ± 0.0000
|2025-01-09 14:34:03| Flops: 9894400
|2025-01-09 14:34:03| Params: 37871
|2025-01-09 14:34:03| Inference time: 0.07 ms
|2025-01-09 14:34:03| ********************Experiment Success********************
```

```python
|2025-01-09 14:34:03| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'log': <utils.logger.Logger object at 0x769dd81138f0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': lstm, 'num_classes': 6, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 80, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-09 14:34:03| ********************Experiment Start********************
|2025-01-09 14:37:55| Round=1 BestEpoch=187 Acc=0.7616 F1=0.6642 Precision=0.7232 Recall=0.6509 Training_time=167.5 s 

|2025-01-09 14:37:55| ********************Experiment Results:********************
|2025-01-09 14:37:55| Acc: 0.7616 ± 0.0000
|2025-01-09 14:37:55| F1: 0.6642 ± 0.0000
|2025-01-09 14:37:55| P: 0.7232 ± 0.0000
|2025-01-09 14:37:55| Recall: 0.6509 ± 0.0000
|2025-01-09 14:37:55| train_time: 167.5442 ± 0.0000
|2025-01-09 14:37:56| Flops: 23203840
|2025-01-09 14:37:56| Params: 89381
|2025-01-09 14:37:56| Inference time: 0.08 ms
|2025-01-09 14:37:56| ********************Experiment Success********************
```

```python
|2025-01-09 14:37:56| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'log': <utils.logger.Logger object at 0x769ddab02390>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': lstm, 'num_classes': 6, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 100, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-09 14:37:56| ********************Experiment Start********************
|2025-01-09 14:42:48| Round=1 BestEpoch=199 Acc=0.7776 F1=0.6873 Precision=0.7164 Recall=0.6733 Training_time=231.8 s 

|2025-01-09 14:42:48| ********************Experiment Results:********************
|2025-01-09 14:42:48| Acc: 0.7776 ± 0.0000
|2025-01-09 14:42:48| F1: 0.6873 ± 0.0000
|2025-01-09 14:42:48| P: 0.7164 ± 0.0000
|2025-01-09 14:42:48| Recall: 0.6733 ± 0.0000
|2025-01-09 14:42:48| train_time: 231.7801 ± 0.0000
|2025-01-09 14:42:49| Flops: 35148800
|2025-01-09 14:42:49| Params: 135721
|2025-01-09 14:42:49| Inference time: 0.08 ms
|2025-01-09 14:42:49| ********************Experiment Success********************
```

```python
|2025-01-09 14:42:49| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'log': <utils.logger.Logger object at 0x769d3ce554c0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': cnn, 'num_classes': 6, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 0,
}
|2025-01-09 14:42:49| ********************Experiment Start********************
