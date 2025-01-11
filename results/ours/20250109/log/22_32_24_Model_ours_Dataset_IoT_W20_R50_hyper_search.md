```python
|2025-01-09 22:32:24| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d862eb9faa0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 22:32:24| ********************Experiment Start********************
|2025-01-09 22:40:27| Round=1 BestEpoch=222 Acc=0.8994 F1=0.8488 Precision=0.8548 Recall=0.8453 Training_time=362.2 s 

|2025-01-09 22:40:27| ********************Experiment Results:********************
|2025-01-09 22:40:27| Acc: 0.8994 ± 0.0000
|2025-01-09 22:40:27| F1: 0.8488 ± 0.0000
|2025-01-09 22:40:27| P: 0.8548 ± 0.0000
|2025-01-09 22:40:27| Recall: 0.8453 ± 0.0000
|2025-01-09 22:40:27| train_time: 362.1979 ± 0.0000
|2025-01-09 22:40:28| Flops: 38700928
|2025-01-09 22:40:28| Params: 73471
|2025-01-09 22:40:28| Inference time: 0.31 ms
|2025-01-09 22:40:28| ********************Experiment Success********************
```

