```python
|2025-01-13 00:06:43| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7bcb750cab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 8, 'verbose': 10,
}
|2025-01-13 00:06:43| ********************Experiment Start********************
|2025-01-13 00:18:39| Round=1 BestEpoch=129 Acc=0.9256 F1=0.8879 Precision=0.8858 Recall=0.8903 Training_time=522.8 s 

|2025-01-13 00:18:39| ********************Experiment Results:********************
|2025-01-13 00:18:39| Acc: 0.9256 ± 0.0000
|2025-01-13 00:18:39| F1: 0.8879 ± 0.0000
|2025-01-13 00:18:39| P: 0.8858 ± 0.0000
|2025-01-13 00:18:39| Recall: 0.8903 ± 0.0000
|2025-01-13 00:18:39| train_time: 522.8105 ± 0.0000
|2025-01-13 00:18:40| Skip the efficiency calculation
|2025-01-13 00:18:40| ********************Experiment Success********************
```

