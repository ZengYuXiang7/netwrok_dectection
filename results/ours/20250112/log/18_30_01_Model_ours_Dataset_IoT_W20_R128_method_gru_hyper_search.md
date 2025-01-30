```python
|2025-01-12 18:30:01| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x757d5025ecc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-12 18:30:01| ********************Experiment Start********************
|2025-01-12 18:39:57| Round=1 BestEpoch= 93 Acc=0.9273 F1=0.8901 Precision=0.8884 Recall=0.8922 Training_time=406.3 s 

|2025-01-12 18:39:57| ********************Experiment Results:********************
|2025-01-12 18:39:57| Acc: 0.9273 ± 0.0000
|2025-01-12 18:39:57| F1: 0.8901 ± 0.0000
|2025-01-12 18:39:57| P: 0.8884 ± 0.0000
|2025-01-12 18:39:57| Recall: 0.8922 ± 0.0000
|2025-01-12 18:39:57| train_time: 406.2804 ± 0.0000
|2025-01-12 18:39:58| Skip the efficiency calculation
|2025-01-12 18:39:58| ********************Experiment Success********************
```

