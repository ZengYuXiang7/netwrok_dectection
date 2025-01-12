```python
|2025-01-12 10:14:41| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x74c0ef1bab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-12 10:14:41| ********************Experiment Start********************
|2025-01-12 10:29:02| Round=1 BestEpoch=138 Acc=0.9248 F1=0.8855 Precision=0.8862 Recall=0.8855 Training_time=639.1 s 

|2025-01-12 10:29:02| ********************Experiment Results:********************
|2025-01-12 10:29:02| Acc: 0.9248 ± 0.0000
|2025-01-12 10:29:02| F1: 0.8855 ± 0.0000
|2025-01-12 10:29:02| P: 0.8862 ± 0.0000
|2025-01-12 10:29:02| Recall: 0.8855 ± 0.0000
|2025-01-12 10:29:02| train_time: 639.1160 ± 0.0000
|2025-01-12 10:29:03| Skip the efficiency calculation
|2025-01-12 10:29:03| ********************Experiment Success********************
```

