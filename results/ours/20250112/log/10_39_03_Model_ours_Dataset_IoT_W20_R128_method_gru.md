```python
|2025-01-12 10:39:03| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x12fdf686ab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 4, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-12 10:39:03| ********************Experiment Start********************
|2025-01-12 10:39:05| Acc=0.9238 F1=0.8834 Precision=0.8839 Recall=0.8837 time=379.7 s 
|2025-01-12 10:39:05| ********************Experiment Results:********************
|2025-01-12 10:39:05| Acc: 0.9238 ± 0.0000
|2025-01-12 10:39:05| F1: 0.8834 ± 0.0000
|2025-01-12 10:39:05| P: 0.8839 ± 0.0000
|2025-01-12 10:39:05| Recall: 0.8837 ± 0.0000
|2025-01-12 10:39:05| train_time: 379.7497 ± 0.0000
|2025-01-12 10:39:06| Skip the efficiency calculation
|2025-01-12 10:39:07| ********************Experiment Success********************
```

