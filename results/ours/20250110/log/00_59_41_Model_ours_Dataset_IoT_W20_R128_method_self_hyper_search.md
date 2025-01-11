```python
|2025-01-10 00:59:41| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7171cfce06e0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 128,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': self, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 00:59:41| ********************Experiment Start********************
|2025-01-10 01:04:08| Round=1 BestEpoch=108 Acc=0.9025 F1=0.8554 Precision=0.8553 Recall=0.8561 Training_time=179.8 s 

|2025-01-10 01:04:08| ********************Experiment Results:********************
|2025-01-10 01:04:08| Acc: 0.9025 ± 0.0000
|2025-01-10 01:04:08| F1: 0.8554 ± 0.0000
|2025-01-10 01:04:08| P: 0.8553 ± 0.0000
|2025-01-10 01:04:08| Recall: 0.8561 ± 0.0000
|2025-01-10 01:04:08| train_time: 179.7732 ± 0.0000
|2025-01-10 01:04:10| Flops: 137043968
|2025-01-10 01:04:10| Params: 426261
|2025-01-10 01:04:10| Inference time: 0.38 ms
|2025-01-10 01:04:10| ********************Experiment Success********************
```

