```python
|2025-01-18 23:17:34| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x76becae10380>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 23:17:34| ********************Experiment Start********************
|2025-01-18 23:17:59| Round=1 BestEpoch= 34 Acc=0.9243 F1=0.6977 Precision=0.7033 Recall=0.6946 Training_time=9.8 s 

|2025-01-18 23:17:59| ********************Experiment Results:********************
|2025-01-18 23:17:59| Acc: 0.9243 ± 0.0000
|2025-01-18 23:17:59| F1: 0.6977 ± 0.0000
|2025-01-18 23:17:59| P: 0.7033 ± 0.0000
|2025-01-18 23:17:59| Recall: 0.6946 ± 0.0000
|2025-01-18 23:17:59| train_time: 9.7612 ± 0.0000
|2025-01-18 23:17:59| Flops: 818176
|2025-01-18 23:17:59| Params: 6264
|2025-01-18 23:17:59| Inference time: 0.05 ms
|2025-01-18 23:18:00| ********************Experiment Success********************
```

