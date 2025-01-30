```python
|2025-01-12 23:20:03| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x75872601c980>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 4, 'verbose': 10,
}
|2025-01-12 23:20:03| ********************Experiment Start********************
|2025-01-12 23:30:52| Round=1 BestEpoch=114 Acc=0.9254 F1=0.8846 Precision=0.8826 Recall=0.8874 Training_time=462.7 s 

|2025-01-12 23:30:52| ********************Experiment Results:********************
|2025-01-12 23:30:52| Acc: 0.9254 ± 0.0000
|2025-01-12 23:30:52| F1: 0.8846 ± 0.0000
|2025-01-12 23:30:52| P: 0.8826 ± 0.0000
|2025-01-12 23:30:52| Recall: 0.8874 ± 0.0000
|2025-01-12 23:30:52| train_time: 462.7362 ± 0.0000
|2025-01-12 23:30:53| Skip the efficiency calculation
|2025-01-12 23:30:53| ********************Experiment Success********************
```

