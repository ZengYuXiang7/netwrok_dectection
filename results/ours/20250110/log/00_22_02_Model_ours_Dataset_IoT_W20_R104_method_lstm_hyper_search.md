```python
|2025-01-10 00:22:02| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7061a50133e0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 104,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': lstm, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 00:22:02| ********************Experiment Start********************
|2025-01-10 00:25:34| Round=1 BestEpoch= 76 Acc=0.8823 F1=0.8344 Precision=0.8334 Recall=0.8377 Training_time=130.7 s 

|2025-01-10 00:25:34| ********************Experiment Results:********************
|2025-01-10 00:25:34| Acc: 0.8823 ± 0.0000
|2025-01-10 00:25:34| F1: 0.8344 ± 0.0000
|2025-01-10 00:25:34| P: 0.8334 ± 0.0000
|2025-01-10 00:25:34| Recall: 0.8377 ± 0.0000
|2025-01-10 00:25:34| train_time: 130.6967 ± 0.0000
|2025-01-10 00:25:35| Flops: 542603776
|2025-01-10 00:25:35| Params: 457413
|2025-01-10 00:25:35| Inference time: 0.36 ms
|2025-01-10 00:25:35| ********************Experiment Success********************
```

