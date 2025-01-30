```python
|2025-01-12 23:45:37| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a84b58546b0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 6, 'verbose': 10,
}
|2025-01-12 23:45:37| ********************Experiment Start********************
|2025-01-12 23:58:15| Round=1 BestEpoch=137 Acc=0.9271 F1=0.8903 Precision=0.8910 Recall=0.8902 Training_time=561.3 s 

|2025-01-12 23:58:15| ********************Experiment Results:********************
|2025-01-12 23:58:15| Acc: 0.9271 ± 0.0000
|2025-01-12 23:58:15| F1: 0.8903 ± 0.0000
|2025-01-12 23:58:15| P: 0.8910 ± 0.0000
|2025-01-12 23:58:15| Recall: 0.8902 ± 0.0000
|2025-01-12 23:58:15| train_time: 561.2756 ± 0.0000
|2025-01-12 23:58:15| Skip the efficiency calculation
|2025-01-12 23:58:16| ********************Experiment Success********************
```

