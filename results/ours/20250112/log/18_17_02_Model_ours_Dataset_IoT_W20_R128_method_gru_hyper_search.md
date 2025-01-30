```python
|2025-01-12 18:17:02| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7ec4e84b66c0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-12 18:17:02| ********************Experiment Start********************
|2025-01-12 18:29:22| Round=1 BestEpoch=122 Acc=0.9241 F1=0.8832 Precision=0.8810 Recall=0.8860 Training_time=533.0 s 

|2025-01-12 18:29:22| ********************Experiment Results:********************
|2025-01-12 18:29:22| Acc: 0.9241 ± 0.0000
|2025-01-12 18:29:22| F1: 0.8832 ± 0.0000
|2025-01-12 18:29:22| P: 0.8810 ± 0.0000
|2025-01-12 18:29:22| Recall: 0.8860 ± 0.0000
|2025-01-12 18:29:22| train_time: 532.9504 ± 0.0000
|2025-01-12 18:29:26| Skip the efficiency calculation
|2025-01-12 18:29:26| ********************Experiment Success********************
```

