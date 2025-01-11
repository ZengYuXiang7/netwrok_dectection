```python
|2025-01-09 23:35:15| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d8ca559bda0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': external, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:35:15| ********************Experiment Start********************
|2025-01-09 23:35:16| Acc=0.5238 F1=0.4841 Precision=0.5133 Recall=0.5320 time=94.0 s 
|2025-01-09 23:35:16| ********************Experiment Results:********************
|2025-01-09 23:35:16| Acc: 0.5238 ± 0.0000
|2025-01-09 23:35:16| F1: 0.4841 ± 0.0000
|2025-01-09 23:35:16| P: 0.5133 ± 0.0000
|2025-01-09 23:35:16| Recall: 0.5320 ± 0.0000
|2025-01-09 23:35:16| train_time: 93.9606 ± 0.0000
|2025-01-09 23:35:17| Flops: 78139392
|2025-01-09 23:35:17| Params: 125077
|2025-01-09 23:35:17| Inference time: 0.38 ms
|2025-01-09 23:35:17| ********************Experiment Success********************
```

