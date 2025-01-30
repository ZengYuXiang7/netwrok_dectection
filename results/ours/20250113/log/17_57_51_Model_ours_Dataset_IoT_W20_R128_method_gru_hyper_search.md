```python
|2025-01-13 17:57:51| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x75a31a046720>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 16, 'verbose': 10,
}
|2025-01-13 17:57:51| ********************Experiment Start********************
|2025-01-13 18:13:15| Round=1 BestEpoch=147 Acc=0.9109 F1=0.8613 Precision=0.8667 Recall=0.8608 Training_time=697.8 s 

|2025-01-13 18:13:15| ********************Experiment Results:********************
|2025-01-13 18:13:15| Acc: 0.9109 ± 0.0000
|2025-01-13 18:13:15| F1: 0.8613 ± 0.0000
|2025-01-13 18:13:15| P: 0.8667 ± 0.0000
|2025-01-13 18:13:15| Recall: 0.8608 ± 0.0000
|2025-01-13 18:13:15| train_time: 697.7840 ± 0.0000
|2025-01-13 18:13:16| Flops: 4387180544
|2025-01-13 18:13:16| Params: 2058965
|2025-01-13 18:13:16| Inference time: 0.83 ms
|2025-01-13 18:13:16| ********************Experiment Success********************
```

