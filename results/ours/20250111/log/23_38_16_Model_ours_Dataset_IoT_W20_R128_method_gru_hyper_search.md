```python
|2025-01-11 23:38:16| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e35bf2d5a00>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 23:38:16| ********************Experiment Start********************
|2025-01-11 23:44:18| Round=1 BestEpoch= 61 Acc=0.9263 F1=0.8855 Precision=0.8833 Recall=0.8883 Training_time=219.3 s 

|2025-01-11 23:44:18| ********************Experiment Results:********************
|2025-01-11 23:44:18| Acc: 0.9263 ± 0.0000
|2025-01-11 23:44:18| F1: 0.8855 ± 0.0000
|2025-01-11 23:44:18| P: 0.8833 ± 0.0000
|2025-01-11 23:44:18| Recall: 0.8883 ± 0.0000
|2025-01-11 23:44:18| train_time: 219.2776 ± 0.0000
|2025-01-11 23:44:18| Skip the efficiency calculation
|2025-01-11 23:44:19| ********************Experiment Success********************
```

