```python
|2025-01-10 01:19:07| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x702294be2120>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 104,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': external, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 01:19:07| ********************Experiment Start********************
|2025-01-10 01:23:25| Round=1 BestEpoch=115 Acc=0.8974 F1=0.8497 Precision=0.8537 Recall=0.8467 Training_time=173.5 s 

|2025-01-10 01:23:25| ********************Experiment Results:********************
|2025-01-10 01:23:25| Acc: 0.8974 ± 0.0000
|2025-01-10 01:23:25| F1: 0.8497 ± 0.0000
|2025-01-10 01:23:25| P: 0.8537 ± 0.0000
|2025-01-10 01:23:25| Recall: 0.8467 ± 0.0000
|2025-01-10 01:23:25| train_time: 173.4794 ± 0.0000
|2025-01-10 01:23:27| Flops: 160184832
|2025-01-10 01:23:27| Params: 309317
|2025-01-10 01:23:27| Inference time: 0.30 ms
|2025-01-10 01:23:28| ********************Experiment Success********************
```

