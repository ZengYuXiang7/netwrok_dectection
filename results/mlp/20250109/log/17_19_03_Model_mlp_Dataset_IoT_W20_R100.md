```python
|2025-01-09 17:19:03| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': False, 'log': <utils.logger.Logger object at 0xdd230c87c50>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': mlp, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 100,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 17:19:03| ********************Experiment Start********************
|2025-01-09 17:19:04| Acc=0.8083 F1=0.7163 Precision=0.7329 Recall=0.7051 time=353.7 s 
|2025-01-09 17:19:04| ********************Experiment Results:********************
|2025-01-09 17:19:04| Acc: 0.8083 ± 0.0000
|2025-01-09 17:19:04| F1: 0.7163 ± 0.0000
|2025-01-09 17:19:04| P: 0.7329 ± 0.0000
|2025-01-09 17:19:04| Recall: 0.7051 ± 0.0000
|2025-01-09 17:19:04| train_time: 353.6937 ± 0.0000
|2025-01-09 17:19:05| Flops: 1917952
|2025-01-09 17:19:05| Params: 14763
|2025-01-09 17:19:05| Inference time: 0.06 ms
|2025-01-09 17:19:05| ********************Experiment Success********************
```

