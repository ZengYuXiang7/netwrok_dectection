```python
|2025-01-11 22:02:51| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7240bbbc3830>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 22:02:51| ********************Experiment Start********************
|2025-01-11 22:16:31| Round=1 BestEpoch=129 Acc=0.9254 F1=0.8882 Precision=0.8886 Recall=0.8881 Training_time=598.2 s 

|2025-01-11 22:16:31| ********************Experiment Results:********************
|2025-01-11 22:16:31| Acc: 0.9254 ± 0.0000
|2025-01-11 22:16:31| F1: 0.8882 ± 0.0000
|2025-01-11 22:16:31| P: 0.8886 ± 0.0000
|2025-01-11 22:16:31| Recall: 0.8881 ± 0.0000
|2025-01-11 22:16:31| train_time: 598.1809 ± 0.0000
|2025-01-11 22:16:31| Skip the efficiency calculation
|2025-01-11 22:16:32| ********************Experiment Success********************
```

