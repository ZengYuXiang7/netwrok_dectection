```python
|2025-01-10 15:15:28| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d05034a1e20>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 20,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 15:15:28| ********************Experiment Start********************
|2025-01-10 15:27:14| Round=1 BestEpoch=307 Acc=0.8940 F1=0.8395 Precision=0.8436 Recall=0.8391 Training_time=559.4 s 

|2025-01-10 15:27:14| ********************Experiment Results:********************
|2025-01-10 15:27:14| Acc: 0.8940 ± 0.0000
|2025-01-10 15:27:14| F1: 0.8395 ± 0.0000
|2025-01-10 15:27:14| P: 0.8436 ± 0.0000
|2025-01-10 15:27:14| Recall: 0.8391 ± 0.0000
|2025-01-10 15:27:14| train_time: 559.3549 ± 0.0000
|2025-01-10 15:27:17| Flops: 17606400
|2025-01-10 15:27:17| Params: 17569
|2025-01-10 15:27:17| Inference time: 0.38 ms
|2025-01-10 15:27:17| ********************Experiment Success********************
```

