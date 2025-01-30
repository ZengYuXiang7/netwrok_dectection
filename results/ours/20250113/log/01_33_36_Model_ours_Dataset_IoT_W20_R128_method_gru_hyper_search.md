```python
|2025-01-13 01:33:36| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7bf956c6ecc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 15, 'verbose': 10,
}
|2025-01-13 01:33:36| ********************Experiment Start********************
|2025-01-13 01:49:36| Round=1 BestEpoch=171 Acc=0.9130 F1=0.8658 Precision=0.8754 Recall=0.8599 Training_time=740.7 s 

|2025-01-13 01:49:36| ********************Experiment Results:********************
|2025-01-13 01:49:36| Acc: 0.9130 ± 0.0000
|2025-01-13 01:49:36| F1: 0.8658 ± 0.0000
|2025-01-13 01:49:36| P: 0.8754 ± 0.0000
|2025-01-13 01:49:36| Recall: 0.8599 ± 0.0000
|2025-01-13 01:49:36| train_time: 740.6867 ± 0.0000
|2025-01-13 01:49:37| Skip the efficiency calculation
|2025-01-13 01:49:37| ********************Experiment Success********************
```

