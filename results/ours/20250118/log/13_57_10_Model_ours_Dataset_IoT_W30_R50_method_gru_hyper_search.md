```python
|2025-01-18 13:57:10| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7fa72e2c2d20>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 13:57:10| ********************Experiment Start********************
|2025-01-18 14:07:54| Round=1 BestEpoch= 94 Acc=0.9044 F1=0.8431 Precision=0.8610 Recall=0.8353 Training_time=467.2 s 

|2025-01-18 14:07:54| ********************Experiment Results:********************
|2025-01-18 14:07:54| Acc: 0.9044 ± 0.0000
|2025-01-18 14:07:54| F1: 0.8431 ± 0.0000
|2025-01-18 14:07:54| P: 0.8610 ± 0.0000
|2025-01-18 14:07:54| Recall: 0.8353 ± 0.0000
|2025-01-18 14:07:54| train_time: 467.1925 ± 0.0000
|2025-01-18 14:07:54| Flops: 914828800
|2025-01-18 14:07:54| Params: 798025
|2025-01-18 14:07:54| Inference time: 1.39 ms
|2025-01-18 14:07:55| ********************Experiment Success********************
```

