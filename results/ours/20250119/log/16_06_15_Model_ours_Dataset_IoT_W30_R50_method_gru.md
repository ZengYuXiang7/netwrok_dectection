```python
|2025-01-19 16:06:15| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x7ca280ab740>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 16:06:15| ********************Experiment Start********************
|2025-01-19 16:06:16| Acc=0.9124 F1=0.8521 Precision=0.8566 Recall=0.8493 time=322.8 s 
|2025-01-19 16:06:16| ********************Experiment Results:********************
|2025-01-19 16:06:16| Acc: 0.9124 ± 0.0000
|2025-01-19 16:06:16| F1: 0.8521 ± 0.0000
|2025-01-19 16:06:16| P: 0.8566 ± 0.0000
|2025-01-19 16:06:16| Recall: 0.8493 ± 0.0000
|2025-01-19 16:06:16| train_time: 322.7947 ± 0.0000
|2025-01-19 16:06:17| Flops: 1444320000
|2025-01-19 16:06:17| Params: 1059175
|2025-01-19 16:06:17| Inference time: 2.32 ms
|2025-01-19 16:06:17| ********************Experiment Success********************
```

