```python
|2025-01-11 23:18:31| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x125d03a7b890>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 4, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 23:18:31| ********************Experiment Start********************
|2025-01-11 23:18:33| Acc=0.9248 F1=0.8866 Precision=0.8858 Recall=0.8876 time=953.2 s 
|2025-01-11 23:18:33| ********************Experiment Results:********************
|2025-01-11 23:18:33| Acc: 0.9248 ± 0.0000
|2025-01-11 23:18:33| F1: 0.8866 ± 0.0000
|2025-01-11 23:18:33| P: 0.8858 ± 0.0000
|2025-01-11 23:18:33| Recall: 0.8876 ± 0.0000
|2025-01-11 23:18:33| train_time: 953.1534 ± 0.0000
|2025-01-11 23:18:35| Skip the efficiency calculation
|2025-01-11 23:18:35| ********************Experiment Success********************
```

