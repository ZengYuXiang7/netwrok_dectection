```python
|2025-01-13 01:49:40| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d29469125d0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 16, 'verbose': 10,
}
|2025-01-13 01:49:40| ********************Experiment Start********************
|2025-01-13 02:04:18| Round=1 BestEpoch=153 Acc=0.9305 F1=0.8938 Precision=0.8941 Recall=0.8941 Training_time=665.6 s 

|2025-01-13 02:04:18| ********************Experiment Results:********************
|2025-01-13 02:04:18| Acc: 0.9305 ± 0.0000
|2025-01-13 02:04:18| F1: 0.8938 ± 0.0000
|2025-01-13 02:04:18| P: 0.8941 ± 0.0000
|2025-01-13 02:04:18| Recall: 0.8941 ± 0.0000
|2025-01-13 02:04:18| train_time: 665.6301 ± 0.0000
|2025-01-13 02:04:19| Skip the efficiency calculation
|2025-01-13 02:04:19| ********************Experiment Success********************
```

