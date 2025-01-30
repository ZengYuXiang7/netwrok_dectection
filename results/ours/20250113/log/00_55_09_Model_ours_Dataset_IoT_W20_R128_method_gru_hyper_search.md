```python
|2025-01-13 00:55:09| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x746b4c2ad970>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 12, 'verbose': 10,
}
|2025-01-13 00:55:09| ********************Experiment Start********************
|2025-01-13 01:12:49| Round=1 BestEpoch=188 Acc=0.9272 F1=0.8898 Precision=0.8912 Recall=0.8893 Training_time=830.8 s 

|2025-01-13 01:12:49| ********************Experiment Results:********************
|2025-01-13 01:12:49| Acc: 0.9272 ± 0.0000
|2025-01-13 01:12:49| F1: 0.8898 ± 0.0000
|2025-01-13 01:12:49| P: 0.8912 ± 0.0000
|2025-01-13 01:12:49| Recall: 0.8893 ± 0.0000
|2025-01-13 01:12:49| train_time: 830.8445 ± 0.0000
|2025-01-13 01:12:52| Skip the efficiency calculation
|2025-01-13 01:12:53| ********************Experiment Success********************
```

