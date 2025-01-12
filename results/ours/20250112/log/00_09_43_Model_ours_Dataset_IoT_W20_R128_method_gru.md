```python
|2025-01-12 00:09:43| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xfa7c7d9ab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-12 00:09:43| ********************Experiment Start********************
|2025-01-12 00:18:24| Round=1 BestEpoch= 84 Acc=0.9248 F1=0.8882 Precision=0.8867 Recall=0.8899 Training_time=345.3 s 

|2025-01-12 00:18:24| ********************Experiment Results:********************
|2025-01-12 00:18:24| Acc: 0.9248 ± 0.0000
|2025-01-12 00:18:24| F1: 0.8882 ± 0.0000
|2025-01-12 00:18:24| P: 0.8867 ± 0.0000
|2025-01-12 00:18:24| Recall: 0.8899 ± 0.0000
|2025-01-12 00:18:24| train_time: 345.2942 ± 0.0000
|2025-01-12 00:18:24| Skip the efficiency calculation
|2025-01-12 00:18:25| ********************Experiment Success********************
```

