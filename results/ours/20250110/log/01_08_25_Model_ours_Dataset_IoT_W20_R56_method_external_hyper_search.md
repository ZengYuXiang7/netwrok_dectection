```python
|2025-01-10 01:08:25| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a2db82df7d0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 56,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': external, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 01:08:25| ********************Experiment Start********************
|2025-01-10 01:13:40| Round=1 BestEpoch=147 Acc=0.8954 F1=0.8411 Precision=0.8510 Recall=0.8353 Training_time=221.7 s 

|2025-01-10 01:13:40| ********************Experiment Results:********************
|2025-01-10 01:13:40| Acc: 0.8954 ± 0.0000
|2025-01-10 01:13:40| F1: 0.8411 ± 0.0000
|2025-01-10 01:13:40| P: 0.8510 ± 0.0000
|2025-01-10 01:13:40| Recall: 0.8353 ± 0.0000
|2025-01-10 01:13:40| train_time: 221.7377 ± 0.0000
|2025-01-10 01:13:41| Flops: 64851456
|2025-01-10 01:13:41| Params: 98021
|2025-01-10 01:13:41| Inference time: 0.30 ms
|2025-01-10 01:13:41| ********************Experiment Success********************
```

