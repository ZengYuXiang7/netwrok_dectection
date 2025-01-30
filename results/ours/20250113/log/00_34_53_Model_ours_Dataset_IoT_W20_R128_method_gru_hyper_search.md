```python
|2025-01-13 00:34:53| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7cabbdad0710>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 11, 'verbose': 10,
}
|2025-01-13 00:34:53| ********************Experiment Start********************
|2025-01-13 00:55:05| Round=1 BestEpoch=221 Acc=0.9282 F1=0.8933 Precision=0.8946 Recall=0.8936 Training_time=967.2 s 

|2025-01-13 00:55:05| ********************Experiment Results:********************
|2025-01-13 00:55:05| Acc: 0.9282 ± 0.0000
|2025-01-13 00:55:05| F1: 0.8933 ± 0.0000
|2025-01-13 00:55:05| P: 0.8946 ± 0.0000
|2025-01-13 00:55:05| Recall: 0.8936 ± 0.0000
|2025-01-13 00:55:05| train_time: 967.2323 ± 0.0000
|2025-01-13 00:55:05| Skip the efficiency calculation
|2025-01-13 00:55:06| ********************Experiment Success********************
```

