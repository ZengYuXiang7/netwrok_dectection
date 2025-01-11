```python
|2025-01-09 16:58:36| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x72267581e180>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': mlp, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 16:58:36| ********************Experiment Start********************
|2025-01-09 17:03:02| Round=1 BestEpoch=248 Acc=0.7610 F1=0.6582 Precision=0.6681 Recall=0.6528 Training_time=185.8 s 

|2025-01-09 17:03:02| ********************Experiment Results:********************
|2025-01-09 17:03:02| Acc: 0.7610 ± 0.0000
|2025-01-09 17:03:02| F1: 0.6582 ± 0.0000
|2025-01-09 17:03:02| P: 0.6681 ± 0.0000
|2025-01-09 17:03:02| Recall: 0.6528 ± 0.0000
|2025-01-09 17:03:02| train_time: 185.7817 ± 0.0000
|2025-01-09 17:03:03| Flops: 708352
|2025-01-09 17:03:03| Params: 5413
|2025-01-09 17:03:03| Inference time: 0.05 ms
|2025-01-09 17:03:03| ********************Experiment Success********************
```

