```python
|2025-01-12 22:57:38| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7ea209326cc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 2, 'verbose': 10,
}
|2025-01-12 22:57:38| ********************Experiment Start********************
|2025-01-12 23:07:45| Round=1 BestEpoch=105 Acc=0.9279 F1=0.8925 Precision=0.8909 Recall=0.8945 Training_time=426.3 s 

|2025-01-12 23:07:45| ********************Experiment Results:********************
|2025-01-12 23:07:45| Acc: 0.9279 ± 0.0000
|2025-01-12 23:07:45| F1: 0.8925 ± 0.0000
|2025-01-12 23:07:45| P: 0.8909 ± 0.0000
|2025-01-12 23:07:45| Recall: 0.8945 ± 0.0000
|2025-01-12 23:07:45| train_time: 426.2917 ± 0.0000
|2025-01-12 23:07:46| Skip the efficiency calculation
|2025-01-12 23:07:47| ********************Experiment Success********************
```

