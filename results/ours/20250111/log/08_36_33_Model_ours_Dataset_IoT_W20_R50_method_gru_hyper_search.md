```python
|2025-01-11 08:36:33| {
     'Ablation': 0, 'bidirectional': False, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e8f17018230>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 50, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': gru, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 08:36:33| ********************Experiment Start********************
|2025-01-11 08:44:04| Round=1 BestEpoch=168 Acc=0.9168 F1=0.8734 Precision=0.8740 Recall=0.8743 Training_time=333.2 s 

|2025-01-11 08:44:04| ********************Experiment Results:********************
|2025-01-11 08:44:04| Acc: 0.9168 ± 0.0000
|2025-01-11 08:44:04| F1: 0.8734 ± 0.0000
|2025-01-11 08:44:04| P: 0.8740 ± 0.0000
|2025-01-11 08:44:04| Recall: 0.8743 ± 0.0000
|2025-01-11 08:44:04| train_time: 333.1637 ± 0.0000
|2025-01-11 08:44:05| Flops: 102028800
|2025-01-11 08:44:05| Params: 98175
|2025-01-11 08:44:05| Inference time: 0.33 ms
|2025-01-11 08:44:05| ********************Experiment Success********************
```

