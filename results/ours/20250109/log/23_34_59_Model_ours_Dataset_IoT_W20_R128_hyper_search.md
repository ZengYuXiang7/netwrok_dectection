```python
|2025-01-09 23:34:59| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x78fbb4200c20>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 128,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': self, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:34:59| ********************Experiment Start********************
|2025-01-09 23:35:01| Acc=0.1322 F1=0.1293 Precision=0.2409 Recall=0.1504 time=149.0 s 
|2025-01-09 23:35:01| ********************Experiment Results:********************
|2025-01-09 23:35:01| Acc: 0.1322 ± 0.0000
|2025-01-09 23:35:01| F1: 0.1293 ± 0.0000
|2025-01-09 23:35:01| P: 0.2409 ± 0.0000
|2025-01-09 23:35:01| Recall: 0.1504 ± 0.0000
|2025-01-09 23:35:01| train_time: 148.9575 ± 0.0000
|2025-01-09 23:35:02| Flops: 137043968
|2025-01-09 23:35:02| Params: 426261
|2025-01-09 23:35:02| Inference time: 0.47 ms
|2025-01-09 23:35:02| ********************Experiment Success********************
```

