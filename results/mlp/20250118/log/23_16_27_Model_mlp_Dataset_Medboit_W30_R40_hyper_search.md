```python
|2025-01-18 23:16:27| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e44307e1fa0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 23:16:27| ********************Experiment Start********************
|2025-01-18 23:16:58| Round=1 BestEpoch= 52 Acc=0.9209 F1=0.5839 Precision=0.5893 Recall=0.5797 Training_time=14.8 s 

|2025-01-18 23:16:58| ********************Experiment Results:********************
|2025-01-18 23:16:58| Acc: 0.9209 ± 0.0000
|2025-01-18 23:16:58| F1: 0.5839 ± 0.0000
|2025-01-18 23:16:58| P: 0.5893 ± 0.0000
|2025-01-18 23:16:58| Recall: 0.5797 ± 0.0000
|2025-01-18 23:16:58| train_time: 14.8062 ± 0.0000
|2025-01-18 23:16:58| Flops: 444416
|2025-01-18 23:16:58| Params: 3384
|2025-01-18 23:16:58| Inference time: 0.05 ms
|2025-01-18 23:16:59| ********************Experiment Success********************
```

