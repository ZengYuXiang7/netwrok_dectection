```python
|2025-01-11 14:26:45| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x78b9f57737d0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 128, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': gru, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 14:26:45| ********************Experiment Start********************
|2025-01-11 14:36:55| Round=1 BestEpoch=151 Acc=0.9208 F1=0.8778 Precision=0.8780 Recall=0.8779 Training_time=449.9 s 

|2025-01-11 14:36:55| ********************Experiment Results:********************
|2025-01-11 14:36:55| Acc: 0.9208 ± 0.0000
|2025-01-11 14:36:55| F1: 0.8778 ± 0.0000
|2025-01-11 14:36:55| P: 0.8780 ± 0.0000
|2025-01-11 14:36:55| Recall: 0.8779 ± 0.0000
|2025-01-11 14:36:55| train_time: 449.9335 ± 0.0000
|2025-01-11 14:36:56| Skip the efficiency calculation
|2025-01-11 14:36:56| ********************Experiment Success********************
```

