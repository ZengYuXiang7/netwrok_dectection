```python
|2025-01-11 19:19:29| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x672bdc02b10>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.0025, 'model': graphiot, 'num_classes': 6,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 19:19:29| ********************Experiment Start********************
|2025-01-11 19:32:20| Round=1 BestEpoch= 67 Acc=0.1459 F1=0.1014 Precision=0.2012 Recall=0.1303 Training_time=455.0 s 

|2025-01-11 19:32:20| ********************Experiment Results:********************
|2025-01-11 19:32:20| Acc: 0.1459 ± 0.0000
|2025-01-11 19:32:20| F1: 0.1014 ± 0.0000
|2025-01-11 19:32:20| P: 0.2012 ± 0.0000
|2025-01-11 19:32:20| Recall: 0.1303 ± 0.0000
|2025-01-11 19:32:20| train_time: 455.0418 ± 0.0000
|2025-01-11 19:32:42| Skip the efficiency calculation
|2025-01-11 19:32:44| ********************Experiment Success********************
```

