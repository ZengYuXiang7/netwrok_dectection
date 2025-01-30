```python
|2025-01-18 15:48:57| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7336f501fe90>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 8, 'verbose': 1,
}
|2025-01-18 15:48:57| ********************Experiment Start********************
|2025-01-18 16:03:09| Round=1 BestEpoch=101 Acc=0.9061 F1=0.8398 Precision=0.8516 Recall=0.8340 Training_time=631.3 s 

|2025-01-18 16:03:09| ********************Experiment Results:********************
|2025-01-18 16:03:09| Acc: 0.9061 ± 0.0000
|2025-01-18 16:03:09| F1: 0.8398 ± 0.0000
|2025-01-18 16:03:09| P: 0.8516 ± 0.0000
|2025-01-18 16:03:09| Recall: 0.8340 ± 0.0000
|2025-01-18 16:03:09| train_time: 631.2673 ± 0.0000
|2025-01-18 16:03:10| Flops: 1147212800
|2025-01-18 16:03:10| Params: 1026675
|2025-01-18 16:03:10| Inference time: 1.82 ms
|2025-01-18 16:03:10| ********************Experiment Success********************
```

