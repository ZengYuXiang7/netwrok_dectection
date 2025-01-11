```python
|2025-01-10 01:23:30| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7152c0285160>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 128,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': external, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 01:23:30| ********************Experiment Start********************
|2025-01-10 01:27:10| Round=1 BestEpoch= 93 Acc=0.8989 F1=0.8490 Precision=0.8579 Recall=0.8432 Training_time=140.0 s 

|2025-01-10 01:27:10| ********************Experiment Results:********************
|2025-01-10 01:27:10| Acc: 0.8989 ± 0.0000
|2025-01-10 01:27:10| F1: 0.8490 ± 0.0000
|2025-01-10 01:27:10| P: 0.8579 ± 0.0000
|2025-01-10 01:27:10| Recall: 0.8432 ± 0.0000
|2025-01-10 01:27:10| train_time: 139.9720 ± 0.0000
|2025-01-10 01:27:10| Flops: 221896704
|2025-01-10 01:27:10| Params: 459029
|2025-01-10 01:27:10| Inference time: 0.30 ms
|2025-01-10 01:27:11| ********************Experiment Success********************
```

