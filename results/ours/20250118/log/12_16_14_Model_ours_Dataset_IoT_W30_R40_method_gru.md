```python
|2025-01-18 12:16:14| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x7fea6a1f3b0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 12:16:14| ********************Experiment Start********************
|2025-01-18 12:16:15| Acc=0.9009 F1=0.8360 Precision=0.8418 Recall=0.8325 time=280.4 s 
|2025-01-18 12:16:15| ********************Experiment Results:********************
|2025-01-18 12:16:15| Acc: 0.9009 ± 0.0000
|2025-01-18 12:16:15| F1: 0.8360 ± 0.0000
|2025-01-18 12:16:15| P: 0.8418 ± 0.0000
|2025-01-18 12:16:15| Recall: 0.8325 ± 0.0000
|2025-01-18 12:16:15| train_time: 280.4377 ± 0.0000
|2025-01-18 12:16:15| Flops: 442988800
|2025-01-18 12:16:15| Params: 162989
|2025-01-18 12:16:15| Inference time: 0.52 ms
|2025-01-18 12:16:15| ********************Experiment Success********************
```

