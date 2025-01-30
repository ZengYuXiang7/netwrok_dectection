```python
|2025-01-18 00:02:44| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x12025bd7ecc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 00:02:44| ********************Experiment Start********************
|2025-01-18 00:02:45| Acc=0.8428 F1=0.7626 Precision=0.7690 Recall=0.7586 time=82.1 s 
|2025-01-18 00:02:45| ********************Experiment Results:********************
|2025-01-18 00:02:45| Acc: 0.8428 ± 0.0000
|2025-01-18 00:02:45| F1: 0.7626 ± 0.0000
|2025-01-18 00:02:45| P: 0.7690 ± 0.0000
|2025-01-18 00:02:45| Recall: 0.7586 ± 0.0000
|2025-01-18 00:02:45| train_time: 82.0810 ± 0.0000
|2025-01-18 00:02:45| Flops: 179020800
|2025-01-18 00:02:45| Params: 82221
|2025-01-18 00:02:45| Inference time: 0.08 ms
|2025-01-18 00:02:45| ********************Experiment Success********************
```

