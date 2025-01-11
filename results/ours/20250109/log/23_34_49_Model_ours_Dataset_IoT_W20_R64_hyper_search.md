```python
|2025-01-09 23:34:49| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7cfcb6a5bbc0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': self, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:34:49| ********************Experiment Start********************
|2025-01-09 23:34:51| Acc=0.1558 F1=0.1451 Precision=0.2432 Recall=0.1786 time=94.0 s 
|2025-01-09 23:34:51| ********************Experiment Results:********************
|2025-01-09 23:34:51| Acc: 0.1558 ± 0.0000
|2025-01-09 23:34:51| F1: 0.1451 ± 0.0000
|2025-01-09 23:34:51| P: 0.2432 ± 0.0000
|2025-01-09 23:34:51| Recall: 0.1786 ± 0.0000
|2025-01-09 23:34:51| train_time: 93.9606 ± 0.0000
|2025-01-09 23:34:51| Flops: 35229696
|2025-01-09 23:34:51| Params: 108693
|2025-01-09 23:34:51| Inference time: 0.47 ms
|2025-01-09 23:34:51| ********************Experiment Success********************
```

