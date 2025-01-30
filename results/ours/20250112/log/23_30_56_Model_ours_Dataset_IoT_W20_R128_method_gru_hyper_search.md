```python
|2025-01-12 23:30:56| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x73d9d6a2ab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 5, 'verbose': 10,
}
|2025-01-12 23:30:56| ********************Experiment Start********************
|2025-01-12 23:45:33| Round=1 BestEpoch=160 Acc=0.9231 F1=0.8842 Precision=0.8840 Recall=0.8848 Training_time=666.6 s 

|2025-01-12 23:45:33| ********************Experiment Results:********************
|2025-01-12 23:45:33| Acc: 0.9231 ± 0.0000
|2025-01-12 23:45:33| F1: 0.8842 ± 0.0000
|2025-01-12 23:45:33| P: 0.8840 ± 0.0000
|2025-01-12 23:45:33| Recall: 0.8848 ± 0.0000
|2025-01-12 23:45:33| train_time: 666.6072 ± 0.0000
|2025-01-12 23:45:33| Skip the efficiency calculation
|2025-01-12 23:45:34| ********************Experiment Success********************
```

