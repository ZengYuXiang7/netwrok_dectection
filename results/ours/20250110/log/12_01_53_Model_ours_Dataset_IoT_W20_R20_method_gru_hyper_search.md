```python
|2025-01-10 12:01:53| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7ac6008f1cd0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 20,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 12:01:53| ********************Experiment Start********************
|2025-01-10 12:13:43| Round=1 BestEpoch=307 Acc=0.8940 F1=0.8395 Precision=0.8436 Recall=0.8391 Training_time=561.3 s 

|2025-01-10 12:13:43| ********************Experiment Results:********************
|2025-01-10 12:13:43| Acc: 0.8940 ± 0.0000
|2025-01-10 12:13:43| F1: 0.8395 ± 0.0000
|2025-01-10 12:13:43| P: 0.8436 ± 0.0000
|2025-01-10 12:13:43| Recall: 0.8391 ± 0.0000
|2025-01-10 12:13:43| train_time: 561.3210 ± 0.0000
|2025-01-10 12:13:45| Flops: 17606400
|2025-01-10 12:13:45| Params: 17569
|2025-01-10 12:13:45| Inference time: 0.39 ms
|2025-01-10 12:13:46| ********************Experiment Success********************
```

