```python
|2025-01-09 20:50:32| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d411d20f410>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 20:50:32| ********************Experiment Start********************
|2025-01-09 20:50:34| Acc=0.9074 F1=0.8600 Precision=0.8622 Recall=0.8600 time=330.4 s 
|2025-01-09 20:50:34| ********************Experiment Results:********************
|2025-01-09 20:50:34| Acc: 0.9074 ± 0.0000
|2025-01-09 20:50:34| F1: 0.8600 ± 0.0000
|2025-01-09 20:50:34| P: 0.8622 ± 0.0000
|2025-01-09 20:50:34| Recall: 0.8600 ± 0.0000
|2025-01-09 20:50:34| train_time: 330.4292 ± 0.0000
|2025-01-09 20:50:35| Flops: 128329600
|2025-01-09 20:50:35| Params: 107871
|2025-01-09 20:50:35| Inference time: 0.42 ms
|2025-01-09 20:50:35| ********************Experiment Success********************
```

