```python
|2025-01-09 17:03:06| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 40,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x78716d12e300>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': mlp, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 17:03:06| ********************Experiment Start********************
|2025-01-09 17:05:44| Round=1 BestEpoch=173 Acc=0.7549 F1=0.6279 Precision=0.6540 Recall=0.6163 Training_time=102.9 s 

|2025-01-09 17:05:44| ********************Experiment Results:********************
|2025-01-09 17:05:44| Acc: 0.7549 ± 0.0000
|2025-01-09 17:05:44| F1: 0.6279 ± 0.0000
|2025-01-09 17:05:44| P: 0.6540 ± 0.0000
|2025-01-09 17:05:44| Recall: 0.6163 ± 0.0000
|2025-01-09 17:05:44| train_time: 102.8863 ± 0.0000
|2025-01-09 17:05:45| Flops: 772352
|2025-01-09 17:05:45| Params: 5913
|2025-01-09 17:05:45| Inference time: 0.06 ms
|2025-01-09 17:05:45| ********************Experiment Success********************
```

