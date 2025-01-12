```python
|2025-01-12 09:35:36| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x73c424a1ab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-12 09:35:36| ********************Experiment Start********************
|2025-01-12 09:43:19| Round=1 BestEpoch= 74 Acc=0.9256 F1=0.8867 Precision=0.8895 Recall=0.8851 Training_time=291.6 s 

|2025-01-12 09:43:19| ********************Experiment Results:********************
|2025-01-12 09:43:19| Acc: 0.9256 ± 0.0000
|2025-01-12 09:43:19| F1: 0.8867 ± 0.0000
|2025-01-12 09:43:19| P: 0.8895 ± 0.0000
|2025-01-12 09:43:19| Recall: 0.8851 ± 0.0000
|2025-01-12 09:43:19| train_time: 291.6290 ± 0.0000
|2025-01-12 09:43:20| Skip the efficiency calculation
|2025-01-12 09:43:20| ********************Experiment Success********************
```

