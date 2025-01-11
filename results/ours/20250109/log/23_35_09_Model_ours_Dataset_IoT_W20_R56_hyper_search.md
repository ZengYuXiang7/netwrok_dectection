```python
|2025-01-09 23:35:09| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a4814d8be00>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 56,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': external, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:35:09| ********************Experiment Start********************
|2025-01-09 23:35:11| Acc=0.6891 F1=0.6039 Precision=0.6290 Recall=0.5999 time=394.0 s 
|2025-01-09 23:35:11| ********************Experiment Results:********************
|2025-01-09 23:35:11| Acc: 0.6891 ± 0.0000
|2025-01-09 23:35:11| F1: 0.6039 ± 0.0000
|2025-01-09 23:35:11| P: 0.6290 ± 0.0000
|2025-01-09 23:35:11| Recall: 0.5999 ± 0.0000
|2025-01-09 23:35:11| train_time: 393.9708 ± 0.0000
|2025-01-09 23:35:12| Flops: 64851456
|2025-01-09 23:35:12| Params: 98021
|2025-01-09 23:35:12| Inference time: 0.39 ms
|2025-01-09 23:35:12| ********************Experiment Success********************
```

