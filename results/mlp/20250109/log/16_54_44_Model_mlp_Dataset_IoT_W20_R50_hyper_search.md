```python
|2025-01-09 16:54:44| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 1, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x78045f7da2d0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': mlp, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 16:54:44| ********************Experiment Start********************
|2025-01-09 16:54:45| Acc=0.7632 F1=0.6571 Precision=0.6761 Recall=0.6491 time=224.9 s 
|2025-01-09 16:54:45| ********************Experiment Results:********************
|2025-01-09 16:54:45| Acc: 0.7632 ± 0.0000
|2025-01-09 16:54:45| F1: 0.6571 ± 0.0000
|2025-01-09 16:54:45| P: 0.6761 ± 0.0000
|2025-01-09 16:54:45| Recall: 0.6491 ± 0.0000
|2025-01-09 16:54:45| train_time: 224.9043 ± 0.0000
|2025-01-09 16:54:46| Flops: 644352
|2025-01-09 16:54:46| Params: 4913
|2025-01-09 16:54:46| Inference time: 0.07 ms
|2025-01-09 16:54:46| ********************Experiment Success********************
```

