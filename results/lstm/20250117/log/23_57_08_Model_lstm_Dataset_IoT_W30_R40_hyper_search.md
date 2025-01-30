```python
|2025-01-17 23:57:08| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x77b0cc7e7b30>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-17 23:57:08| ********************Experiment Start********************
|2025-01-17 23:57:08| Acc=0.8364 F1=0.7535 Precision=0.7708 Recall=0.7485 time=120.4 s 
|2025-01-17 23:57:08| ********************Experiment Results:********************
|2025-01-17 23:57:08| Acc: 0.8364 ± 0.0000
|2025-01-17 23:57:08| F1: 0.7535 ± 0.0000
|2025-01-17 23:57:08| P: 0.7708 ± 0.0000
|2025-01-17 23:57:08| Recall: 0.7485 ± 0.0000
|2025-01-17 23:57:08| train_time: 120.4246 ± 0.0000
|2025-01-17 23:57:09| Flops: 82483200
|2025-01-17 23:57:09| Params: 45221
|2025-01-17 23:57:09| Inference time: 0.08 ms
|2025-01-17 23:57:09| ********************Experiment Success********************
```

