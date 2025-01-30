```python
|2025-01-27 16:45:05| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x71478c7fbbf0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': True, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-27 16:45:05| ********************Experiment Start********************
|2025-01-27 16:48:49| Round=1 BestEpoch=175 Acc=0.8605 F1=0.8398 Precision=0.8505 Recall=0.8325 Training_time=158.5 s 

|2025-01-27 16:51:59| Round=2 BestEpoch=141 Acc=0.8497 F1=0.8094 Precision=0.8296 Recall=0.8020 Training_time=129.3 s 

|2025-01-27 16:51:59| ********************Experiment Results:********************
|2025-01-27 16:51:59| Acc: 0.8551 ± 0.0054
|2025-01-27 16:51:59| F1: 0.8246 ± 0.0152
|2025-01-27 16:51:59| P: 0.8401 ± 0.0104
|2025-01-27 16:51:59| Recall: 0.8172 ± 0.0153
|2025-01-27 16:51:59| train_time: 143.8842 ± 14.5849
|2025-01-27 16:51:59| Flops: 210176
|2025-01-27 16:51:59| Params: 3213
|2025-01-27 16:51:59| Inference time: 0.04 ms
|2025-01-27 16:52:00| ********************Experiment Success********************
```

