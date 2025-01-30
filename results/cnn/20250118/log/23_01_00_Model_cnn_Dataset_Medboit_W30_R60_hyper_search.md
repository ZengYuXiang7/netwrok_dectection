```python
|2025-01-18 23:01:00| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b28d3488560>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 23:01:00| ********************Experiment Start********************
|2025-01-18 23:02:45| Round=1 BestEpoch=215 Acc=0.9393 F1=0.7343 Precision=0.7517 Recall=0.7190 Training_time=68.5 s 

|2025-01-18 23:02:45| ********************Experiment Results:********************
|2025-01-18 23:02:45| Acc: 0.9393 ± 0.0000
|2025-01-18 23:02:45| F1: 0.7343 ± 0.0000
|2025-01-18 23:02:45| P: 0.7517 ± 0.0000
|2025-01-18 23:02:45| Recall: 0.7190 ± 0.0000
|2025-01-18 23:02:45| train_time: 68.5260 ± 0.0000
|2025-01-18 23:02:45| Flops: 44305920
|2025-01-18 23:02:45| Params: 11828
|2025-01-18 23:02:45| Inference time: 0.08 ms
|2025-01-18 23:02:46| ********************Experiment Success********************
```

