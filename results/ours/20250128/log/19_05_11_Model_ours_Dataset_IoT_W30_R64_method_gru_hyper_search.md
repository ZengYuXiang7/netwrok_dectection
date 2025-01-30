```python
|2025-01-28 19:05:11| {
     'ablation': 1, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7fca05fbfd10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-28 19:05:11| ********************Experiment Start********************
|2025-01-28 19:08:16| Round=1 BestEpoch=179 Ac=0.8601 Pr=0.7954 Rc=0.7809 F1=0.7860 Training_time=117.1 s 

|2025-01-28 19:11:15| Round=2 BestEpoch=170 Ac=0.8696 Pr=0.8117 Rc=0.8038 F1=0.8054 Training_time=112.3 s 

|2025-01-28 19:11:15| ********************Experiment Results:********************
|2025-01-28 19:11:15| AC: 0.8649 ± 0.0047
|2025-01-28 19:11:15| PR: 0.8036 ± 0.0081
|2025-01-28 19:11:15| RC: 0.7924 ± 0.0115
|2025-01-28 19:11:15| F1: 0.7957 ± 0.0097
|2025-01-28 19:11:15| train_time: 114.7002 ± 2.4059
|2025-01-28 19:11:15| Flops: 136151040
|2025-01-28 19:11:15| Params: 77589
|2025-01-28 19:11:15| Inference time: 0.08 ms
|2025-01-28 19:11:16| ********************Experiment Success********************
```

