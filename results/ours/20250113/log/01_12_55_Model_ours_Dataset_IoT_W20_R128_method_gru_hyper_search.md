```python
|2025-01-13 01:12:55| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7de7c699b140>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 13, 'verbose': 10,
}
|2025-01-13 01:12:55| ********************Experiment Start********************
|2025-01-13 01:23:26| Round=1 BestEpoch=100 Acc=0.9116 F1=0.8658 Precision=0.8721 Recall=0.8664 Training_time=440.4 s 

|2025-01-13 01:23:26| ********************Experiment Results:********************
|2025-01-13 01:23:26| Acc: 0.9116 ± 0.0000
|2025-01-13 01:23:26| F1: 0.8658 ± 0.0000
|2025-01-13 01:23:26| P: 0.8721 ± 0.0000
|2025-01-13 01:23:26| Recall: 0.8664 ± 0.0000
|2025-01-13 01:23:26| train_time: 440.3631 ± 0.0000
|2025-01-13 01:23:27| Skip the efficiency calculation
|2025-01-13 01:23:28| ********************Experiment Success********************
```

