```python
|2025-01-09 23:35:25| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x78bc09f9c9e0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 128,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': external, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:35:25| ********************Experiment Start********************
|2025-01-09 23:35:26| Acc=0.5342 F1=0.4733 Precision=0.5204 Recall=0.5119 time=149.0 s 
|2025-01-09 23:35:26| ********************Experiment Results:********************
|2025-01-09 23:35:26| Acc: 0.5342 ± 0.0000
|2025-01-09 23:35:26| F1: 0.4733 ± 0.0000
|2025-01-09 23:35:26| P: 0.5204 ± 0.0000
|2025-01-09 23:35:26| Recall: 0.5119 ± 0.0000
|2025-01-09 23:35:26| train_time: 148.9575 ± 0.0000
|2025-01-09 23:35:27| Flops: 221896704
|2025-01-09 23:35:27| Params: 459029
|2025-01-09 23:35:27| Inference time: 0.36 ms
|2025-01-09 23:35:27| ********************Experiment Success********************
```

