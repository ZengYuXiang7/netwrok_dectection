```python
|2025-01-18 22:54:54| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7fa722b0f9e0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 22:54:54| ********************Experiment Start********************
|2025-01-18 22:55:21| Round=1 BestEpoch= 34 Acc=0.9243 F1=0.6977 Precision=0.7033 Recall=0.6946 Training_time=11.5 s 

|2025-01-18 22:55:21| ********************Experiment Results:********************
|2025-01-18 22:55:21| Acc: 0.9243 ± 0.0000
|2025-01-18 22:55:21| F1: 0.6977 ± 0.0000
|2025-01-18 22:55:21| P: 0.7033 ± 0.0000
|2025-01-18 22:55:21| Recall: 0.6946 ± 0.0000
|2025-01-18 22:55:21| train_time: 11.4980 ± 0.0000
|2025-01-18 22:55:21| Flops: 818176
|2025-01-18 22:55:21| Params: 6264
|2025-01-18 22:55:21| Inference time: 0.05 ms
|2025-01-18 22:55:22| ********************Experiment Success********************
```

