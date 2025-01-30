```python
|2025-01-18 23:15:56| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a2fb492de50>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 23:15:56| ********************Experiment Start********************
|2025-01-18 23:15:57| Acc=0.9209 F1=0.5839 Precision=0.5893 Recall=0.5797 time=15.1 s 
|2025-01-18 23:15:57| ********************Experiment Results:********************
|2025-01-18 23:15:57| Acc: 0.9209 ± 0.0000
|2025-01-18 23:15:57| F1: 0.5839 ± 0.0000
|2025-01-18 23:15:57| P: 0.5893 ± 0.0000
|2025-01-18 23:15:57| Recall: 0.5797 ± 0.0000
|2025-01-18 23:15:57| train_time: 15.0660 ± 0.0000
|2025-01-18 23:15:57| Flops: 444416
|2025-01-18 23:15:57| Params: 3384
|2025-01-18 23:15:57| Inference time: 0.06 ms
|2025-01-18 23:15:57| ********************Experiment Success********************
```

