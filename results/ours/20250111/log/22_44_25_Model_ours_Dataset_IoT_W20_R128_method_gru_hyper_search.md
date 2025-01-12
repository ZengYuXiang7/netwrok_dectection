```python
|2025-01-11 22:44:25| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x74c0fb4bab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 22:44:25| ********************Experiment Start********************
|2025-01-11 22:58:01| Round=1 BestEpoch=127 Acc=0.9274 F1=0.8893 Precision=0.8892 Recall=0.8899 Training_time=595.3 s 

|2025-01-11 22:58:01| ********************Experiment Results:********************
|2025-01-11 22:58:01| Acc: 0.9274 ± 0.0000
|2025-01-11 22:58:01| F1: 0.8893 ± 0.0000
|2025-01-11 22:58:01| P: 0.8892 ± 0.0000
|2025-01-11 22:58:01| Recall: 0.8899 ± 0.0000
|2025-01-11 22:58:01| train_time: 595.2620 ± 0.0000
|2025-01-11 22:58:02| Skip the efficiency calculation
|2025-01-11 22:58:02| ********************Experiment Success********************
```

