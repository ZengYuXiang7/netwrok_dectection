```python
|2025-01-17 23:57:11| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c8bc6ba3680>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-17 23:57:11| ********************Experiment Start********************
|2025-01-18 00:00:36| Round=1 BestEpoch=249 Acc=0.8501 F1=0.7714 Precision=0.7759 Recall=0.7691 Training_time=152.2 s 

|2025-01-18 00:00:36| ********************Experiment Results:********************
|2025-01-18 00:00:36| Acc: 0.8501 ± 0.0000
|2025-01-18 00:00:36| F1: 0.7714 ± 0.0000
|2025-01-18 00:00:36| P: 0.7759 ± 0.0000
|2025-01-18 00:00:36| Recall: 0.7691 ± 0.0000
|2025-01-18 00:00:36| train_time: 152.2056 ± 0.0000
|2025-01-18 00:00:36| Flops: 126144000
|2025-01-18 00:00:36| Params: 62521
|2025-01-18 00:00:36| Inference time: 0.07 ms
|2025-01-18 00:00:37| ********************Experiment Success********************
```

