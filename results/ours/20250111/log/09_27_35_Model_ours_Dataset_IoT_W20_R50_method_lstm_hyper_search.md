```python
|2025-01-11 09:27:35| {
     'Ablation': 0, 'bidirectional': False, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a2b228cfce0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 50, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': lstm, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 09:27:35| ********************Experiment Start********************
|2025-01-11 09:36:24| Round=1 BestEpoch=200 Acc=0.9078 F1=0.8606 Precision=0.8637 Recall=0.8594 Training_time=402.0 s 

|2025-01-11 09:36:24| ********************Experiment Results:********************
|2025-01-11 09:36:24| Acc: 0.9078 ± 0.0000
|2025-01-11 09:36:24| F1: 0.8606 ± 0.0000
|2025-01-11 09:36:24| P: 0.8637 ± 0.0000
|2025-01-11 09:36:24| Recall: 0.8594 ± 0.0000
|2025-01-11 09:36:24| train_time: 401.9585 ± 0.0000
|2025-01-11 09:36:25| Flops: 128396800
|2025-01-11 09:36:25| Params: 108375
|2025-01-11 09:36:25| Inference time: 0.34 ms
|2025-01-11 09:36:26| ********************Experiment Success********************
```

