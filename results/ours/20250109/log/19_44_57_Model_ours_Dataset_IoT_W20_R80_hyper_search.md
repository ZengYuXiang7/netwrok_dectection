```python
|2025-01-09 19:44:57| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x728760d93aa0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 80,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 19:44:57| ********************Experiment Start********************
|2025-01-09 19:54:14| Round=1 BestEpoch=272 Acc=0.8801 F1=0.8249 Precision=0.8292 Recall=0.8228 Training_time=427.8 s 

|2025-01-09 19:54:14| ********************Experiment Results:********************
|2025-01-09 19:54:14| Acc: 0.8801 ± 0.0000
|2025-01-09 19:54:14| F1: 0.8249 ± 0.0000
|2025-01-09 19:54:14| P: 0.8292 ± 0.0000
|2025-01-09 19:54:14| Recall: 0.8228 ± 0.0000
|2025-01-09 19:54:14| train_time: 427.7558 ± 0.0000
|2025-01-09 19:54:15| Flops: 223810560
|2025-01-09 19:54:15| Params: 233461
|2025-01-09 19:54:15| Inference time: 0.28 ms
|2025-01-09 19:54:16| ********************Experiment Success********************
```

