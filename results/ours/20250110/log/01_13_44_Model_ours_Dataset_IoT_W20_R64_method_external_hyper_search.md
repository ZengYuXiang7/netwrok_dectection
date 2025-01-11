```python
|2025-01-10 01:13:44| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x76112eb45fd0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': external, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 01:13:44| ********************Experiment Start********************
|2025-01-10 01:19:03| Round=1 BestEpoch=149 Acc=0.9007 F1=0.8548 Precision=0.8576 Recall=0.8532 Training_time=224.5 s 

|2025-01-10 01:19:03| ********************Experiment Results:********************
|2025-01-10 01:19:03| Acc: 0.9007 ± 0.0000
|2025-01-10 01:19:03| F1: 0.8548 ± 0.0000
|2025-01-10 01:19:03| P: 0.8576 ± 0.0000
|2025-01-10 01:19:03| Recall: 0.8532 ± 0.0000
|2025-01-10 01:19:03| train_time: 224.4862 ± 0.0000
|2025-01-10 01:19:04| Flops: 78139392
|2025-01-10 01:19:04| Params: 125077
|2025-01-10 01:19:04| Inference time: 0.30 ms
|2025-01-10 01:19:04| ********************Experiment Success********************
```

