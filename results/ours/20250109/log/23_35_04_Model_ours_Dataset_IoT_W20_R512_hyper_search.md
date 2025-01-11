```python
|2025-01-09 23:35:04| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7297660ab260>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 512,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': self, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:35:04| ********************Experiment Start********************
|2025-01-09 23:35:06| Acc=0.8135 F1=0.7323 Precision=0.7560 Recall=0.7269 time=574.8 s 
|2025-01-09 23:35:06| ********************Experiment Results:********************
|2025-01-09 23:35:06| Acc: 0.8135 ± 0.0000
|2025-01-09 23:35:06| F1: 0.7323 ± 0.0000
|2025-01-09 23:35:06| P: 0.7560 ± 0.0000
|2025-01-09 23:35:06| Recall: 0.7269 ± 0.0000
|2025-01-09 23:35:06| train_time: 574.7676 ± 0.0000
|2025-01-09 23:35:07| Flops: 2146205696
|2025-01-09 23:35:07| Params: 6718485
|2025-01-09 23:35:07| Inference time: 0.48 ms
|2025-01-09 23:35:07| ********************Experiment Success********************
```

