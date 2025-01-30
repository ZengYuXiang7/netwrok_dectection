```python
|2025-01-13 01:23:30| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x751fd6d6eb40>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 14, 'verbose': 10,
}
|2025-01-13 01:23:30| ********************Experiment Start********************
|2025-01-13 01:33:32| Round=1 BestEpoch= 95 Acc=0.8318 F1=0.7519 Precision=0.7652 Recall=0.7471 Training_time=414.2 s 

|2025-01-13 01:33:32| ********************Experiment Results:********************
|2025-01-13 01:33:32| Acc: 0.8318 ± 0.0000
|2025-01-13 01:33:32| F1: 0.7519 ± 0.0000
|2025-01-13 01:33:32| P: 0.7652 ± 0.0000
|2025-01-13 01:33:32| Recall: 0.7471 ± 0.0000
|2025-01-13 01:33:32| train_time: 414.2243 ± 0.0000
|2025-01-13 01:33:33| Skip the efficiency calculation
|2025-01-13 01:33:33| ********************Experiment Success********************
```

