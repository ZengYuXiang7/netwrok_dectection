```python
|2025-01-27 16:30:24| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x754f7aadfe00>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 30, 'record': True, 'retrain': True, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-27 16:30:24| ********************Experiment Start********************
|2025-01-27 16:37:28| Round=1 BestEpoch=365 Acc=0.8419 F1=0.8203 Precision=0.8458 Recall=0.8026 Training_time=324.4 s 

|2025-01-27 16:40:01| Round=2 BestEpoch=112 Acc=0.8118 F1=0.7833 Precision=0.8127 Recall=0.7692 Training_time=99.9 s 

|2025-01-27 16:40:01| ********************Experiment Results:********************
|2025-01-27 16:40:01| Acc: 0.8269 ± 0.0150
|2025-01-27 16:40:01| F1: 0.8018 ± 0.0185
|2025-01-27 16:40:01| P: 0.8293 ± 0.0166
|2025-01-27 16:40:01| Recall: 0.7859 ± 0.0167
|2025-01-27 16:40:01| train_time: 212.1726 ± 112.2500
|2025-01-27 16:40:01| Flops: 128256
|2025-01-27 16:40:01| Params: 1953
|2025-01-27 16:40:01| Inference time: 0.04 ms
|2025-01-27 16:40:02| ********************Experiment Success********************
```

