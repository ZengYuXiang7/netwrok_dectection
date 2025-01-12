```python
|2025-01-12 10:29:06| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a603d28bc80>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 4, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-12 10:29:06| ********************Experiment Start********************
|2025-01-12 10:38:59| Round=1 BestEpoch= 71 Acc=0.9268 F1=0.8887 Precision=0.8882 Recall=0.8898 Training_time=379.7 s 

|2025-01-12 10:38:59| ********************Experiment Results:********************
|2025-01-12 10:38:59| Acc: 0.9268 ± 0.0000
|2025-01-12 10:38:59| F1: 0.8887 ± 0.0000
|2025-01-12 10:38:59| P: 0.8882 ± 0.0000
|2025-01-12 10:38:59| Recall: 0.8898 ± 0.0000
|2025-01-12 10:38:59| train_time: 379.7497 ± 0.0000
|2025-01-12 10:39:00| Skip the efficiency calculation
|2025-01-12 10:39:00| ********************Experiment Success********************
```

