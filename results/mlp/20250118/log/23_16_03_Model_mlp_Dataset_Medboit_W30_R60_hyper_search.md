```python
|2025-01-18 23:16:03| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7eb3e318fa40>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 23:16:03| ********************Experiment Start********************
|2025-01-18 23:16:03| Acc=0.9243 F1=0.6977 Precision=0.7033 Recall=0.6946 time=11.5 s 
|2025-01-18 23:16:03| ********************Experiment Results:********************
|2025-01-18 23:16:03| Acc: 0.9243 ± 0.0000
|2025-01-18 23:16:03| F1: 0.6977 ± 0.0000
|2025-01-18 23:16:03| P: 0.7033 ± 0.0000
|2025-01-18 23:16:03| Recall: 0.6946 ± 0.0000
|2025-01-18 23:16:03| train_time: 11.4980 ± 0.0000
|2025-01-18 23:16:03| Flops: 818176
|2025-01-18 23:16:03| Params: 6264
|2025-01-18 23:16:03| Inference time: 0.06 ms
|2025-01-18 23:16:03| ********************Experiment Success********************
```

