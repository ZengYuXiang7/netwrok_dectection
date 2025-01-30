```python
|2025-01-20 17:26:45| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x747c251fe450>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 8, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 17:26:45| ********************Experiment Start********************
|2025-01-20 17:39:22| Round=1 BestEpoch=140 Acc=0.9267 F1=0.8757 Precision=0.8802 Recall=0.8727 Training_time=530.0 s 

|2025-01-20 17:54:24| Round=2 BestEpoch=176 Acc=0.9226 F1=0.8696 Precision=0.8746 Recall=0.8663 Training_time=667.1 s 

|2025-01-20 17:54:24| ********************Experiment Results:********************
|2025-01-20 17:54:24| Acc: 0.9246 ± 0.0020
|2025-01-20 17:54:24| F1: 0.8727 ± 0.0030
|2025-01-20 17:54:24| P: 0.8774 ± 0.0028
|2025-01-20 17:54:24| Recall: 0.8695 ± 0.0032
|2025-01-20 17:54:24| train_time: 598.5585 ± 68.5150
|2025-01-20 17:54:24| Flops: 1115185152
|2025-01-20 17:54:24| Params: 972309
|2025-01-20 17:54:24| Inference time: 1.17 ms
|2025-01-20 17:54:25| ********************Experiment Success********************
```

