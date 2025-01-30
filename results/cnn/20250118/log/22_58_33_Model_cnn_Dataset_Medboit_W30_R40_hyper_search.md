```python
|2025-01-18 22:58:33| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x70414a0c1d90>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 22:58:33| ********************Experiment Start********************
|2025-01-18 23:00:09| Round=1 BestEpoch=195 Acc=0.9287 F1=0.7213 Precision=0.7358 Recall=0.7098 Training_time=61.3 s 

|2025-01-18 23:00:09| ********************Experiment Results:********************
|2025-01-18 23:00:09| Acc: 0.9287 ± 0.0000
|2025-01-18 23:00:09| F1: 0.7213 ± 0.0000
|2025-01-18 23:00:09| P: 0.7358 ± 0.0000
|2025-01-18 23:00:09| Recall: 0.7098 ± 0.0000
|2025-01-18 23:00:09| train_time: 61.2683 ± 0.0000
|2025-01-18 23:00:09| Flops: 20321280
|2025-01-18 23:00:09| Params: 5488
|2025-01-18 23:00:09| Inference time: 0.09 ms
|2025-01-18 23:00:09| ********************Experiment Success********************
```

