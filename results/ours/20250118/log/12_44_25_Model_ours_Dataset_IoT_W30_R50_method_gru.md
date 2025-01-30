```python
|2025-01-18 12:44:25| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xc68ed29c3b0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 12:44:25| ********************Experiment Start********************
|2025-01-18 12:44:26| Acc=0.8970 F1=0.8279 Precision=0.8371 Recall=0.8238 time=360.9 s 
|2025-01-18 12:44:26| ********************Experiment Results:********************
|2025-01-18 12:44:26| Acc: 0.8970 ± 0.0000
|2025-01-18 12:44:26| F1: 0.8279 ± 0.0000
|2025-01-18 12:44:26| P: 0.8371 ± 0.0000
|2025-01-18 12:44:26| Recall: 0.8238 ± 0.0000
|2025-01-18 12:44:26| train_time: 360.8976 ± 0.0000
|2025-01-18 12:44:26| Flops: 1234790400
|2025-01-18 12:44:26| Params: 833025
|2025-01-18 12:44:26| Inference time: 1.68 ms
|2025-01-18 12:44:26| ********************Experiment Success********************
```

