```python
|2025-01-17 20:41:09| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c67eca18bf0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-17 20:41:09| ********************Experiment Start********************
|2025-01-17 20:43:37| Round=1 BestEpoch= 33 Acc=0.9068 F1=0.8465 Precision=0.8560 Recall=0.8396 Training_time=71.2 s 

|2025-01-17 20:43:37| ********************Experiment Results:********************
|2025-01-17 20:43:37| Acc: 0.9068 ± 0.0000
|2025-01-17 20:43:37| F1: 0.8465 ± 0.0000
|2025-01-17 20:43:37| P: 0.8560 ± 0.0000
|2025-01-17 20:43:37| Recall: 0.8396 ± 0.0000
|2025-01-17 20:43:37| train_time: 71.1658 ± 0.0000
|2025-01-17 20:43:37| Flops: 6572773376
|2025-01-17 20:43:37| Params: 2202965
|2025-01-17 20:43:37| Inference time: 0.54 ms
|2025-01-17 20:43:37| ********************Experiment Success********************
```

