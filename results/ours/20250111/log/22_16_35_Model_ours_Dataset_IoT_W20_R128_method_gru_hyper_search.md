```python
|2025-01-11 22:16:35| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e0f3611ecc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 4, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 22:16:35| ********************Experiment Start********************
|2025-01-11 22:26:25| Round=1 BestEpoch= 71 Acc=0.9241 F1=0.8843 Precision=0.8846 Recall=0.8845 Training_time=377.2 s 

|2025-01-11 22:26:25| ********************Experiment Results:********************
|2025-01-11 22:26:25| Acc: 0.9241 ± 0.0000
|2025-01-11 22:26:25| F1: 0.8843 ± 0.0000
|2025-01-11 22:26:25| P: 0.8846 ± 0.0000
|2025-01-11 22:26:25| Recall: 0.8845 ± 0.0000
|2025-01-11 22:26:25| train_time: 377.1591 ± 0.0000
|2025-01-11 22:26:26| Skip the efficiency calculation
|2025-01-11 22:26:26| ********************Experiment Success********************
```

