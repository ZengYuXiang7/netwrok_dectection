```python
|2025-01-12 09:53:14| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a9f5ecafc80>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 4, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-12 09:53:14| ********************Experiment Start********************
|2025-01-12 10:06:32| Round=1 BestEpoch=108 Acc=0.9255 F1=0.8889 Precision=0.8890 Recall=0.8895 Training_time=569.0 s 

|2025-01-12 10:06:32| ********************Experiment Results:********************
|2025-01-12 10:06:32| Acc: 0.9255 ± 0.0000
|2025-01-12 10:06:32| F1: 0.8889 ± 0.0000
|2025-01-12 10:06:32| P: 0.8890 ± 0.0000
|2025-01-12 10:06:32| Recall: 0.8895 ± 0.0000
|2025-01-12 10:06:32| train_time: 569.0133 ± 0.0000
|2025-01-12 10:06:33| Skip the efficiency calculation
|2025-01-12 10:06:34| ********************Experiment Success********************
```

