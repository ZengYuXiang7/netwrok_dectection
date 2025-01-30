```python
|2025-01-29 19:31:43| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x1090fbfcbf80>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 19:31:43| ********************Experiment Start********************
|2025-01-29 19:36:37| Round=1 BestEpoch= 68 Ac=0.9957 Pr=0.7778 Rc=0.7379 F1=0.7542 Training_time=156.7 s 

|2025-01-29 19:40:24| Round=2 BestEpoch= 41 Ac=0.9948 Pr=0.7272 Rc=0.7014 F1=0.6946 Training_time=94.4 s 

|2025-01-29 19:40:24| ********************Experiment Results:********************
|2025-01-29 19:40:24| AC: 0.9952 ± 0.0005
|2025-01-29 19:40:24| PR: 0.7525 ± 0.0253
|2025-01-29 19:40:24| RC: 0.7196 ± 0.0183
|2025-01-29 19:40:24| F1: 0.7244 ± 0.0298
|2025-01-29 19:40:24| train_time: 125.5433 ± 31.1731
|2025-01-29 19:40:24| Flops: 493835264
|2025-01-29 19:40:24| Params: 429218
|2025-01-29 19:40:24| Inference time: 0.91 ms
|2025-01-29 19:40:25| ********************Experiment Success********************
```

