```python
|2025-01-18 23:17:01| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x716d78401e80>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 23:17:01| ********************Experiment Start********************
|2025-01-18 23:17:32| Round=1 BestEpoch= 50 Acc=0.9256 F1=0.6967 Precision=0.7077 Recall=0.6892 Training_time=14.6 s 

|2025-01-18 23:17:32| ********************Experiment Results:********************
|2025-01-18 23:17:32| Acc: 0.9256 ± 0.0000
|2025-01-18 23:17:32| F1: 0.6967 ± 0.0000
|2025-01-18 23:17:32| P: 0.7077 ± 0.0000
|2025-01-18 23:17:32| Recall: 0.6892 ± 0.0000
|2025-01-18 23:17:32| train_time: 14.5863 ± 0.0000
|2025-01-18 23:17:32| Flops: 618496
|2025-01-18 23:17:32| Params: 4724
|2025-01-18 23:17:32| Inference time: 0.05 ms
|2025-01-18 23:17:32| ********************Experiment Success********************
```

