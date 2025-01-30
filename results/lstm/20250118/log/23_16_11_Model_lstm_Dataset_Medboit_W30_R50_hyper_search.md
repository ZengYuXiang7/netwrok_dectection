```python
|2025-01-18 23:16:11| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7fe1c88b5040>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 23:16:11| ********************Experiment Start********************
|2025-01-18 23:16:12| Acc=0.9390 F1=0.7309 Precision=0.7333 Recall=0.7303 time=44.8 s 
|2025-01-18 23:16:12| ********************Experiment Results:********************
|2025-01-18 23:16:12| Acc: 0.9390 ± 0.0000
|2025-01-18 23:16:12| F1: 0.7309 ± 0.0000
|2025-01-18 23:16:12| P: 0.7333 ± 0.0000
|2025-01-18 23:16:12| Recall: 0.7303 ± 0.0000
|2025-01-18 23:16:12| train_time: 44.7884 ± 0.0000
|2025-01-18 23:16:12| Flops: 123648000
|2025-01-18 23:16:12| Params: 43008
|2025-01-18 23:16:12| Inference time: 0.08 ms
|2025-01-18 23:16:12| ********************Experiment Success********************
```

