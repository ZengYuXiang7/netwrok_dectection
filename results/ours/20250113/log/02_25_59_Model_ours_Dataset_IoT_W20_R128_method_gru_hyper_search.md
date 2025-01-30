```python
|2025-01-13 02:25:59| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x71247db9ab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 19, 'verbose': 10,
}
|2025-01-13 02:25:59| ********************Experiment Start********************
|2025-01-13 02:40:21| Round=1 BestEpoch=245 Acc=0.8083 F1=0.7183 Precision=0.7489 Recall=0.6994 Training_time=656.9 s 

|2025-01-13 02:40:21| ********************Experiment Results:********************
|2025-01-13 02:40:21| Acc: 0.8083 ± 0.0000
|2025-01-13 02:40:21| F1: 0.7183 ± 0.0000
|2025-01-13 02:40:21| P: 0.7489 ± 0.0000
|2025-01-13 02:40:21| Recall: 0.6994 ± 0.0000
|2025-01-13 02:40:21| train_time: 656.8794 ± 0.0000
|2025-01-13 02:40:21| Skip the efficiency calculation
|2025-01-13 02:40:22| ********************Experiment Success********************
```

