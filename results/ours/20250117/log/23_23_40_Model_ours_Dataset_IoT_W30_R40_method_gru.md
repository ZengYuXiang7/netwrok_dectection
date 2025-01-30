```python
|2025-01-17 23:23:40| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xec8911a6150>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-17 23:23:40| ********************Experiment Start********************
|2025-01-17 23:23:41| Acc=0.8959 F1=0.8328 Precision=0.8398 Recall=0.8278 time=494.4 s 
|2025-01-17 23:23:41| ********************Experiment Results:********************
|2025-01-17 23:23:41| Acc: 0.8959 ± 0.0000
|2025-01-17 23:23:41| F1: 0.8328 ± 0.0000
|2025-01-17 23:23:41| P: 0.8398 ± 0.0000
|2025-01-17 23:23:41| Recall: 0.8278 ± 0.0000
|2025-01-17 23:23:41| train_time: 494.3789 ± 0.0000
|2025-01-17 23:23:41| Flops: 753982720
|2025-01-17 23:23:41| Params: 429149
|2025-01-17 23:23:41| Inference time: 1.38 ms
|2025-01-17 23:23:41| ********************Experiment Success********************
```

