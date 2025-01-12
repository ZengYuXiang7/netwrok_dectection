```python
|2025-01-11 14:36:59| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xac26cc99eb0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 128, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'seq_method': gru, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 14:36:59| ********************Experiment Start********************
|2025-01-11 14:37:01| Acc=0.9195 F1=0.8765 Precision=0.8772 Recall=0.8761 time=449.9 s 
|2025-01-11 14:37:01| ********************Experiment Results:********************
|2025-01-11 14:37:01| Acc: 0.9195 ± 0.0000
|2025-01-11 14:37:01| F1: 0.8765 ± 0.0000
|2025-01-11 14:37:01| P: 0.8772 ± 0.0000
|2025-01-11 14:37:01| Recall: 0.8761 ± 0.0000
|2025-01-11 14:37:01| train_time: 449.9335 ± 0.0000
|2025-01-11 14:37:03| Skip the efficiency calculation
|2025-01-11 14:37:03| ********************Experiment Success********************
```

