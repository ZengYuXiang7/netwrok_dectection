```python
|2025-01-11 18:33:35| {
     'Ablation': 0, 'bs': 150, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x14411331c560>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.0005, 'model': dapp, 'num_classes': 6,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 18:33:35| ********************Experiment Start********************
|2025-01-11 19:19:02| Round=1 BestEpoch=481 Acc=0.7124 F1=0.6094 Precision=0.6754 Recall=0.5809 Training_time=2223.0 s 

|2025-01-11 19:19:02| ********************Experiment Results:********************
|2025-01-11 19:19:02| Acc: 0.7124 ± 0.0000
|2025-01-11 19:19:02| F1: 0.6094 ± 0.0000
|2025-01-11 19:19:02| P: 0.6754 ± 0.0000
|2025-01-11 19:19:02| Recall: 0.5809 ± 0.0000
|2025-01-11 19:19:02| train_time: 2222.9879 ± 0.0000
|2025-01-11 19:19:25| Skip the efficiency calculation
|2025-01-11 19:19:27| ********************Experiment Success********************
```

