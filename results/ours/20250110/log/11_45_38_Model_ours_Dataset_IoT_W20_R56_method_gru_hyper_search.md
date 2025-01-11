```python
|2025-01-10 11:45:38| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7ba166408590>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 56,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 11:45:38| ********************Experiment Start********************
|2025-01-10 11:53:28| Round=1 BestEpoch=191 Acc=0.9057 F1=0.8561 Precision=0.8595 Recall=0.8537 Training_time=353.1 s 

|2025-01-10 11:53:28| ********************Experiment Results:********************
|2025-01-10 11:53:28| Acc: 0.9057 ± 0.0000
|2025-01-10 11:53:28| F1: 0.8561 ± 0.0000
|2025-01-10 11:53:28| P: 0.8595 ± 0.0000
|2025-01-10 11:53:28| Recall: 0.8537 ± 0.0000
|2025-01-10 11:53:28| train_time: 353.0765 ± 0.0000
|2025-01-10 11:53:29| Flops: 127317120
|2025-01-10 11:53:29| Params: 122493
|2025-01-10 11:53:29| Inference time: 0.40 ms
|2025-01-10 11:53:29| ********************Experiment Success********************
```

