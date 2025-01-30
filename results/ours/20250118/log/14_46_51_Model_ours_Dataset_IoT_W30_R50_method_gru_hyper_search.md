```python
|2025-01-18 14:46:51| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x75fa4b446e10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 3, 'verbose': 1,
}
|2025-01-18 14:46:51| ********************Experiment Start********************
|2025-01-18 14:58:58| Round=1 BestEpoch= 63 Acc=0.9078 F1=0.8479 Precision=0.8526 Recall=0.8465 Training_time=475.5 s 

|2025-01-18 14:58:58| ********************Experiment Results:********************
|2025-01-18 14:58:58| Acc: 0.9078 ± 0.0000
|2025-01-18 14:58:58| F1: 0.8479 ± 0.0000
|2025-01-18 14:58:58| P: 0.8526 ± 0.0000
|2025-01-18 14:58:58| Recall: 0.8465 ± 0.0000
|2025-01-18 14:58:58| train_time: 475.5024 ± 0.0000
|2025-01-18 14:58:59| Flops: 1582406400
|2025-01-18 14:58:59| Params: 1255025
|2025-01-18 14:58:59| Inference time: 2.09 ms
|2025-01-18 14:58:59| ********************Experiment Success********************
```

