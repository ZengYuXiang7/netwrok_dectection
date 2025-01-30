```python
|2025-01-18 23:16:08| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7df7b64af710>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 23:16:08| ********************Experiment Start********************
|2025-01-18 23:16:09| Acc=0.9297 F1=0.7137 Precision=0.7236 Recall=0.7078 time=37.4 s 
|2025-01-18 23:16:09| ********************Experiment Results:********************
|2025-01-18 23:16:09| Acc: 0.9297 ± 0.0000
|2025-01-18 23:16:09| F1: 0.7137 ± 0.0000
|2025-01-18 23:16:09| P: 0.7236 ± 0.0000
|2025-01-18 23:16:09| Recall: 0.7078 ± 0.0000
|2025-01-18 23:16:09| train_time: 37.3750 ± 0.0000
|2025-01-18 23:16:09| Flops: 80486400
|2025-01-18 23:16:09| Params: 29608
|2025-01-18 23:16:09| Inference time: 0.08 ms
|2025-01-18 23:16:09| ********************Experiment Success********************
```

