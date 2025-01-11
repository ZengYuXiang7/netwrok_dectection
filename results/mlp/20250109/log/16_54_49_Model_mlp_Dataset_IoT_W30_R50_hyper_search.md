```python
|2025-01-09 16:54:49| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 1, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7f7f74350920>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': mlp, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 16:54:49| ********************Experiment Start********************
|2025-01-09 16:54:50| Acc=0.5746 F1=0.4054 Precision=0.4781 Recall=0.4075 time=0.8 s 
|2025-01-09 16:54:50| ********************Experiment Results:********************
|2025-01-09 16:54:50| Acc: 0.5746 ± 0.0000
|2025-01-09 16:54:50| F1: 0.4054 ± 0.0000
|2025-01-09 16:54:50| P: 0.4781 ± 0.0000
|2025-01-09 16:54:50| Recall: 0.4075 ± 0.0000
|2025-01-09 16:54:50| train_time: 0.7665 ± 0.0000
|2025-01-09 16:54:51| Flops: 708352
|2025-01-09 16:54:51| Params: 5413
|2025-01-09 16:54:51| Inference time: 0.07 ms
|2025-01-09 16:54:51| ********************Experiment Success********************
```

