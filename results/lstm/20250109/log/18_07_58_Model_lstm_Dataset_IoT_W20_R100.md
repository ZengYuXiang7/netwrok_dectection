```python
|2025-01-09 18:07:58| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': False, 'log': <utils.logger.Logger object at 0x114917c76ba0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': lstm, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 100,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 18:07:58| ********************Experiment Start********************
|2025-01-09 18:08:00| Acc=0.8701 F1=0.8110 Precision=0.8142 Recall=0.8090 time=125.8 s 
|2025-01-09 18:08:00| ********************Experiment Results:********************
|2025-01-09 18:08:00| Acc: 0.8701 ± 0.0000
|2025-01-09 18:08:00| F1: 0.8110 ± 0.0000
|2025-01-09 18:08:00| P: 0.8142 ± 0.0000
|2025-01-09 18:08:00| Recall: 0.8090 ± 0.0000
|2025-01-09 18:08:00| train_time: 125.7835 ± 0.0000
|2025-01-09 18:08:01| Flops: 321792000
|2025-01-09 18:08:01| Params: 164021
|2025-01-09 18:08:01| Inference time: 0.08 ms
|2025-01-09 18:08:01| ********************Experiment Success********************
```

