```python
|2025-01-12 17:49:25| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x713d32080bf0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-12 17:49:25| ********************Experiment Start********************
|2025-01-12 18:01:08| Round=1 BestEpoch=116 Acc=0.9260 F1=0.8895 Precision=0.8906 Recall=0.8890 Training_time=504.6 s 

|2025-01-12 18:01:08| ********************Experiment Results:********************
|2025-01-12 18:01:08| Acc: 0.9260 ± 0.0000
|2025-01-12 18:01:08| F1: 0.8895 ± 0.0000
|2025-01-12 18:01:08| P: 0.8906 ± 0.0000
|2025-01-12 18:01:08| Recall: 0.8890 ± 0.0000
|2025-01-12 18:01:08| train_time: 504.6345 ± 0.0000
|2025-01-12 18:01:12| Skip the efficiency calculation
|2025-01-12 18:01:12| ********************Experiment Success********************
```

