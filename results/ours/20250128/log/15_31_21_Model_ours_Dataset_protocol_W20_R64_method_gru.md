```python
|2025-01-28 15:31:21| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': protocol, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x7b721c37fb0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-28 15:31:21| ********************Experiment Start********************
|2025-01-28 15:31:56| Round=1 BestEpoch= 66 Ac=0.6642 Pr=0.6525 Rc=0.6265 F1=0.6339 Training_time=12.4 s 

|2025-01-28 15:32:38| Round=2 BestEpoch= 92 Ac=0.7007 Pr=0.7351 Rc=0.7158 F1=0.7225 Training_time=17.2 s 

|2025-01-28 15:32:38| ********************Experiment Results:********************
|2025-01-28 15:32:38| AC: 0.6825 ± 0.0182
|2025-01-28 15:32:38| PR: 0.6938 ± 0.0413
|2025-01-28 15:32:38| RC: 0.6711 ± 0.0446
|2025-01-28 15:32:38| F1: 0.6782 ± 0.0443
|2025-01-28 15:32:38| train_time: 14.8410 ± 2.3919
|2025-01-28 15:32:38| Flops: 743473152
|2025-01-28 15:32:38| Params: 648204
|2025-01-28 15:32:38| Inference time: 0.89 ms
|2025-01-28 15:32:39| ********************Experiment Success********************
```

