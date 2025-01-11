```python
|2025-01-09 23:34:44| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7be1cd69a930>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 56,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': self, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:34:44| ********************Experiment Start********************
|2025-01-09 23:34:45| Acc=0.2833 F1=0.1830 Precision=0.1907 Recall=0.2097 time=394.0 s 
|2025-01-09 23:34:45| ********************Experiment Results:********************
|2025-01-09 23:34:45| Acc: 0.2833 ± 0.0000
|2025-01-09 23:34:45| F1: 0.1830 ± 0.0000
|2025-01-09 23:34:45| P: 0.1907 ± 0.0000
|2025-01-09 23:34:45| Recall: 0.2097 ± 0.0000
|2025-01-09 23:34:45| train_time: 393.9708 ± 0.0000
|2025-01-09 23:34:46| Flops: 27184640
|2025-01-09 23:34:46| Params: 83685
|2025-01-09 23:34:46| Inference time: 0.47 ms
|2025-01-09 23:34:46| ********************Experiment Success********************
```

