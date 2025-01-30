```python
|2025-01-14 19:11:06| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7eaf409c3ce0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 256, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 19:11:06| ********************Experiment Start********************
|2025-01-14 19:23:05| Round=1 BestEpoch=114 Acc=0.9256 F1=0.8879 Precision=0.8900 Recall=0.8862 Training_time=512.4 s 

|2025-01-14 19:23:05| ********************Experiment Results:********************
|2025-01-14 19:23:05| Acc: 0.9256 ± 0.0000
|2025-01-14 19:23:05| F1: 0.8879 ± 0.0000
|2025-01-14 19:23:05| P: 0.8900 ± 0.0000
|2025-01-14 19:23:05| Recall: 0.8862 ± 0.0000
|2025-01-14 19:23:05| train_time: 512.3833 ± 0.0000
|2025-01-14 19:23:06| Flops: 11670265856
|2025-01-14 19:23:06| Params: 5898389
|2025-01-14 19:23:06| Inference time: 0.88 ms
|2025-01-14 19:23:07| ********************Experiment Success********************
```

