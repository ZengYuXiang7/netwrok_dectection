```python
|2025-01-17 21:53:03| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7caffd64c860>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-17 21:53:03| ********************Experiment Start********************
|2025-01-17 22:17:42| Round=1 BestEpoch=169 Acc=0.8915 F1=0.8257 Precision=0.8337 Recall=0.8206 Training_time=1214.0 s 

|2025-01-17 22:17:42| ********************Experiment Results:********************
|2025-01-17 22:17:42| Acc: 0.8915 ± 0.0000
|2025-01-17 22:17:42| F1: 0.8257 ± 0.0000
|2025-01-17 22:17:42| P: 0.8337 ± 0.0000
|2025-01-17 22:17:42| Recall: 0.8206 ± 0.0000
|2025-01-17 22:17:42| train_time: 1214.0285 ± 0.0000
|2025-01-17 22:17:43| Flops: 1191450880
|2025-01-17 22:17:43| Params: 772789
|2025-01-17 22:17:43| Inference time: 1.98 ms
|2025-01-17 22:17:43| ********************Experiment Success********************
```

