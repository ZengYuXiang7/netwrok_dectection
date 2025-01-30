```python
|2025-01-17 20:51:33| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b4bf6f43410>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 128, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-17 20:51:33| ********************Experiment Start********************
|2025-01-17 20:52:35| Round=1 BestEpoch= 50 Acc=0.8477 F1=0.7698 Precision=0.7820 Recall=0.7619 Training_time=31.4 s 

|2025-01-17 20:52:35| ********************Experiment Results:********************
|2025-01-17 20:52:35| Acc: 0.8477 ± 0.0000
|2025-01-17 20:52:35| F1: 0.7698 ± 0.0000
|2025-01-17 20:52:35| P: 0.7820 ± 0.0000
|2025-01-17 20:52:35| Recall: 0.7619 ± 0.0000
|2025-01-17 20:52:35| train_time: 31.4132 ± 0.0000
|2025-01-17 20:52:35| Flops: 782991360
|2025-01-17 20:52:35| Params: 279829
|2025-01-17 20:52:35| Inference time: 0.07 ms
|2025-01-17 20:52:35| ********************Experiment Success********************
```

