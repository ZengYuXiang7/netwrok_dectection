```python
|2025-01-10 12:00:40| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': False, 'log': <utils.logger.Logger object at 0x10a62f0f7800>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 56,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 12:00:40| ********************Experiment Start********************
|2025-01-10 12:00:42| Acc=0.1341 F1=0.0716 Precision=0.1073 Recall=0.0994 time=353.1 s 
|2025-01-10 12:00:42| ********************Experiment Results:********************
|2025-01-10 12:00:42| Acc: 0.1341 ± 0.0000
|2025-01-10 12:00:42| F1: 0.0716 ± 0.0000
|2025-01-10 12:00:42| P: 0.1073 ± 0.0000
|2025-01-10 12:00:42| Recall: 0.0994 ± 0.0000
|2025-01-10 12:00:42| train_time: 353.0765 ± 0.0000
|2025-01-10 12:00:43| Flops: 127317120
|2025-01-10 12:00:43| Params: 122493
|2025-01-10 12:00:43| Inference time: 0.46 ms
|2025-01-10 12:00:43| ********************Experiment Success********************
```

