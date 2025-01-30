```python
|2025-01-18 23:16:14| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x78233c339c40>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 23:16:14| ********************Experiment Start********************
|2025-01-18 23:16:15| Acc=0.9341 F1=0.7445 Precision=0.7434 Recall=0.7506 time=21.3 s 
|2025-01-18 23:16:15| ********************Experiment Results:********************
|2025-01-18 23:16:15| Acc: 0.9341 ± 0.0000
|2025-01-18 23:16:15| F1: 0.7445 ± 0.0000
|2025-01-18 23:16:15| P: 0.7434 ± 0.0000
|2025-01-18 23:16:15| Recall: 0.7506 ± 0.0000
|2025-01-18 23:16:15| train_time: 21.3189 ± 0.0000
|2025-01-18 23:16:15| Flops: 176025600
|2025-01-18 23:16:15| Params: 58808
|2025-01-18 23:16:15| Inference time: 0.11 ms
|2025-01-18 23:16:15| ********************Experiment Success********************
```

