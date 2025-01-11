```python
|2025-01-09 21:57:46| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x701cf4c1faa0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 100,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 21:57:46| ********************Experiment Start********************
|2025-01-09 21:59:54| Round=1 BestEpoch= 28 Acc=0.8430 F1=0.7905 Precision=0.7924 Recall=0.7940 Training_time=53.2 s 

|2025-01-09 21:59:54| ********************Experiment Results:********************
|2025-01-09 21:59:54| Acc: 0.8430 ± 0.0000
|2025-01-09 21:59:54| F1: 0.7905 ± 0.0000
|2025-01-09 21:59:54| P: 0.7924 ± 0.0000
|2025-01-09 21:59:54| Recall: 0.7940 ± 0.0000
|2025-01-09 21:59:54| train_time: 53.1748 ± 0.0000
|2025-01-09 21:59:55| Flops: 503123200
|2025-01-09 21:59:55| Params: 423421
|2025-01-09 21:59:55| Inference time: 0.38 ms
|2025-01-09 21:59:55| ********************Experiment Success********************
```

