```python
|2025-01-10 11:53:32| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': False, 'log': <utils.logger.Logger object at 0xbe0de877140>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 56,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 11:53:32| ********************Experiment Start********************
|2025-01-10 11:53:34| Acc=0.9004 F1=0.8450 Precision=0.8479 Recall=0.8433 time=353.1 s 
|2025-01-10 11:53:34| ********************Experiment Results:********************
|2025-01-10 11:53:34| Acc: 0.9004 ± 0.0000
|2025-01-10 11:53:34| F1: 0.8450 ± 0.0000
|2025-01-10 11:53:34| P: 0.8479 ± 0.0000
|2025-01-10 11:53:34| Recall: 0.8433 ± 0.0000
|2025-01-10 11:53:34| train_time: 353.0765 ± 0.0000
|2025-01-10 11:53:34| Flops: 127317120
|2025-01-10 11:53:34| Params: 122493
|2025-01-10 11:53:34| Inference time: 0.45 ms
|2025-01-10 11:53:34| ********************Experiment Success********************
```

