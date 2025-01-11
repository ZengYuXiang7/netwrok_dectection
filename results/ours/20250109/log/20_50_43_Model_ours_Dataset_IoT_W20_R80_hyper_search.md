```python
|2025-01-09 20:50:43| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x78f19aeaa330>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 80,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 20:50:43| ********************Experiment Start********************
|2025-01-09 20:55:57| Round=1 BestEpoch=121 Acc=0.9043 F1=0.8522 Precision=0.8538 Recall=0.8540 Training_time=217.2 s 

|2025-01-09 20:55:57| ********************Experiment Results:********************
|2025-01-09 20:55:57| Acc: 0.9043 ± 0.0000
|2025-01-09 20:55:57| F1: 0.8522 ± 0.0000
|2025-01-09 20:55:57| P: 0.8538 ± 0.0000
|2025-01-09 20:55:57| Recall: 0.8540 ± 0.0000
|2025-01-09 20:55:57| train_time: 217.1617 ± 0.0000
|2025-01-09 20:56:00| Flops: 323138560
|2025-01-09 20:56:00| Params: 272181
|2025-01-09 20:56:00| Inference time: 0.36 ms
|2025-01-09 20:56:01| ********************Experiment Success********************
```

