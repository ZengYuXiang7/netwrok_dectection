```python
|2025-01-11 21:44:26| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c989ce20a70>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 21:44:26| ********************Experiment Start********************
|2025-01-11 21:52:29| Round=1 BestEpoch= 64 Acc=0.9195 F1=0.8737 Precision=0.8742 Recall=0.8744 Training_time=295.4 s 

|2025-01-11 21:52:29| ********************Experiment Results:********************
|2025-01-11 21:52:29| Acc: 0.9195 ± 0.0000
|2025-01-11 21:52:29| F1: 0.8737 ± 0.0000
|2025-01-11 21:52:29| P: 0.8742 ± 0.0000
|2025-01-11 21:52:29| Recall: 0.8744 ± 0.0000
|2025-01-11 21:52:29| train_time: 295.4153 ± 0.0000
|2025-01-11 21:52:29| Skip the efficiency calculation
|2025-01-11 21:52:30| ********************Experiment Success********************
```

