```python
|2025-01-19 02:11:12| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x76996f5b3aa0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 02:11:12| ********************Experiment Start********************
|2025-01-19 02:24:18| Round=1 BestEpoch=283 Acc=0.7900 F1=0.6833 Precision=0.7014 Recall=0.6742 Training_time=168.9 s 

|2025-01-19 02:24:18| ********************Experiment Results:********************
|2025-01-19 02:24:18| Acc: 0.7900 ± 0.0000
|2025-01-19 02:24:18| F1: 0.6833 ± 0.0000
|2025-01-19 02:24:18| P: 0.7014 ± 0.0000
|2025-01-19 02:24:18| Recall: 0.6742 ± 0.0000
|2025-01-19 02:24:18| train_time: 168.8942 ± 0.0000
|2025-01-19 02:24:18| Skip the efficiency calculation
|2025-01-19 02:24:19| ********************Experiment Success********************
```

