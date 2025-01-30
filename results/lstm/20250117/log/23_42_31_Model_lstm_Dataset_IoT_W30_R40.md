```python
|2025-01-17 23:42:31| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x1282aa6d5a60>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-17 23:42:31| ********************Experiment Start********************
|2025-01-17 23:45:19| Round=1 BestEpoch=190 Acc=0.8487 F1=0.7666 Precision=0.7833 Recall=0.7609 Training_time=120.4 s 

|2025-01-17 23:45:19| ********************Experiment Results:********************
|2025-01-17 23:45:19| Acc: 0.8487 ± 0.0000
|2025-01-17 23:45:19| F1: 0.7666 ± 0.0000
|2025-01-17 23:45:19| P: 0.7833 ± 0.0000
|2025-01-17 23:45:19| Recall: 0.7609 ± 0.0000
|2025-01-17 23:45:19| train_time: 120.4246 ± 0.0000
|2025-01-17 23:45:19| Flops: 82483200
|2025-01-17 23:45:19| Params: 45221
|2025-01-17 23:45:19| Inference time: 0.07 ms
|2025-01-17 23:45:19| ********************Experiment Success********************
```

