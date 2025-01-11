```python
|2025-01-10 00:25:38| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x727c90ea0aa0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 128,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': lstm, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 00:25:38| ********************Experiment Start********************
|2025-01-10 00:29:31| Round=1 BestEpoch= 87 Acc=0.8972 F1=0.8420 Precision=0.8425 Recall=0.8426 Training_time=148.5 s 

|2025-01-10 00:29:31| ********************Experiment Results:********************
|2025-01-10 00:29:31| Acc: 0.8972 ± 0.0000
|2025-01-10 00:29:31| F1: 0.8420 ± 0.0000
|2025-01-10 00:29:31| P: 0.8425 ± 0.0000
|2025-01-10 00:29:31| Recall: 0.8426 ± 0.0000
|2025-01-10 00:29:31| train_time: 148.4621 ± 0.0000
|2025-01-10 00:29:32| Flops: 818618368
|2025-01-10 00:29:32| Params: 690453
|2025-01-10 00:29:32| Inference time: 0.36 ms
|2025-01-10 00:29:32| ********************Experiment Success********************
```

