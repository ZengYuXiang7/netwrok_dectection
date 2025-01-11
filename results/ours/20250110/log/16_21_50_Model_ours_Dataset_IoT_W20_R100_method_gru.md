```python
|2025-01-10 16:21:50| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': False, 'log': <utils.logger.Logger object at 0x6f0094d4920>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 100,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 16:21:50| ********************Experiment Start********************
|2025-01-10 16:21:51| Acc=0.9168 F1=0.8731 Precision=0.8730 Recall=0.8739 time=239.1 s 
|2025-01-10 16:21:51| ********************Experiment Results:********************
|2025-01-10 16:21:51| Acc: 0.9168 ± 0.0000
|2025-01-10 16:21:51| F1: 0.8731 ± 0.0000
|2025-01-10 16:21:51| P: 0.8730 ± 0.0000
|2025-01-10 16:21:51| Recall: 0.8739 ± 0.0000
|2025-01-10 16:21:51| train_time: 239.0516 ± 0.0000
|2025-01-10 16:21:52| Flops: 398268800
|2025-01-10 16:21:52| Params: 383621
|2025-01-10 16:21:52| Inference time: 0.47 ms
|2025-01-10 16:21:52| ********************Experiment Success********************
```

