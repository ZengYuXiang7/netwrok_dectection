```python
|2025-01-09 18:08:03| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x76f9d9329cd0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': cnn, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 18:08:03| ********************Experiment Start********************
|2025-01-09 18:16:03| Round=1 BestEpoch=299 Acc=0.8454 F1=0.7634 Precision=0.7909 Recall=0.7521 Training_time=354.7 s 

|2025-01-09 18:16:03| ********************Experiment Results:********************
|2025-01-09 18:16:03| Acc: 0.8454 ± 0.0000
|2025-01-09 18:16:03| F1: 0.7634 ± 0.0000
|2025-01-09 18:16:03| P: 0.7909 ± 0.0000
|2025-01-09 18:16:03| Recall: 0.7521 ± 0.0000
|2025-01-09 18:16:03| train_time: 354.6899 ± 0.0000
|2025-01-09 18:16:04| Flops: 20876800
|2025-01-09 18:16:04| Params: 9021
|2025-01-09 18:16:04| Inference time: 0.10 ms
|2025-01-09 18:16:04| ********************Experiment Success********************
```

