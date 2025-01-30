```python
|2025-01-18 23:19:09| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7831fe526cc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 23:19:09| ********************Experiment Start********************
|2025-01-18 23:20:21| Round=1 BestEpoch=136 Acc=0.9401 F1=0.7414 Precision=0.7503 Recall=0.7333 Training_time=45.5 s 

|2025-01-18 23:20:21| ********************Experiment Results:********************
|2025-01-18 23:20:21| Acc: 0.9401 ± 0.0000
|2025-01-18 23:20:21| F1: 0.7414 ± 0.0000
|2025-01-18 23:20:21| P: 0.7503 ± 0.0000
|2025-01-18 23:20:21| Recall: 0.7333 ± 0.0000
|2025-01-18 23:20:21| train_time: 45.4519 ± 0.0000
|2025-01-18 23:20:21| Flops: 123648000
|2025-01-18 23:20:21| Params: 43008
|2025-01-18 23:20:21| Inference time: 0.07 ms
|2025-01-18 23:20:21| ********************Experiment Success********************
```

