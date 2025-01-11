```python
|2025-01-09 21:55:28| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7f8fe07b5760>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 80,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 21:55:28| ********************Experiment Start********************
|2025-01-09 21:57:42| Round=1 BestEpoch= 33 Acc=0.8309 F1=0.7836 Precision=0.7974 Recall=0.7866 Training_time=60.8 s 

|2025-01-09 21:57:42| ********************Experiment Results:********************
|2025-01-09 21:57:42| Acc: 0.8309 ± 0.0000
|2025-01-09 21:57:42| F1: 0.7836 ± 0.0000
|2025-01-09 21:57:42| P: 0.7974 ± 0.0000
|2025-01-09 21:57:42| Recall: 0.7866 ± 0.0000
|2025-01-09 21:57:42| train_time: 60.7905 ± 0.0000
|2025-01-09 21:57:43| Flops: 323957760
|2025-01-09 21:57:43| Params: 272341
|2025-01-09 21:57:43| Inference time: 0.37 ms
|2025-01-09 21:57:43| ********************Experiment Success********************
```

