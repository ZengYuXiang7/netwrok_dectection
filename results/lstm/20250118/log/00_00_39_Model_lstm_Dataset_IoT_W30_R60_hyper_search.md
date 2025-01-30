```python
|2025-01-18 00:00:39| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x72a5fa587bc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 00:00:39| ********************Experiment Start********************
|2025-01-18 00:02:41| Round=1 BestEpoch=135 Acc=0.8516 F1=0.7737 Precision=0.7812 Recall=0.7696 Training_time=82.1 s 

|2025-01-18 00:02:41| ********************Experiment Results:********************
|2025-01-18 00:02:41| Acc: 0.8516 ± 0.0000
|2025-01-18 00:02:41| F1: 0.7737 ± 0.0000
|2025-01-18 00:02:41| P: 0.7812 ± 0.0000
|2025-01-18 00:02:41| Recall: 0.7696 ± 0.0000
|2025-01-18 00:02:41| train_time: 82.0810 ± 0.0000
|2025-01-18 00:02:41| Flops: 179020800
|2025-01-18 00:02:41| Params: 82221
|2025-01-18 00:02:41| Inference time: 0.07 ms
|2025-01-18 00:02:42| ********************Experiment Success********************
```

