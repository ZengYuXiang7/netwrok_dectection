```python
|2025-01-11 23:55:34| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x792c6f7dd610>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 4, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 23:55:34| ********************Experiment Start********************
|2025-01-12 00:09:38| Round=1 BestEpoch=132 Acc=0.9266 F1=0.8911 Precision=0.8897 Recall=0.8929 Training_time=628.1 s 

|2025-01-12 00:09:38| ********************Experiment Results:********************
|2025-01-12 00:09:38| Acc: 0.9266 ± 0.0000
|2025-01-12 00:09:38| F1: 0.8911 ± 0.0000
|2025-01-12 00:09:38| P: 0.8897 ± 0.0000
|2025-01-12 00:09:38| Recall: 0.8929 ± 0.0000
|2025-01-12 00:09:38| train_time: 628.1367 ± 0.0000
|2025-01-12 00:09:40| Skip the efficiency calculation
|2025-01-12 00:09:41| ********************Experiment Success********************
```

