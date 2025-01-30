```python
|2025-01-30 16:29:04| {
     'ablation': 2, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b074a238530>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 60, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-30 16:29:04| ********************Experiment Start********************
|2025-01-30 16:29:28| Round=1 BestEpoch= 62 Ac=0.9029 Pr=0.5357 Rc=0.4641 F1=0.4765 Training_time=7.3 s 

|2025-01-30 16:29:56| Round=2 BestEpoch= 91 Ac=0.8673 Pr=0.5318 Rc=0.5319 F1=0.5311 Training_time=10.5 s 

|2025-01-30 16:29:56| ********************Experiment Results:********************
|2025-01-30 16:29:56| AC: 0.8851 ± 0.0178
|2025-01-30 16:29:56| PR: 0.5337 ± 0.0019
|2025-01-30 16:29:56| RC: 0.4980 ± 0.0339
|2025-01-30 16:29:56| F1: 0.5038 ± 0.0273
|2025-01-30 16:29:56| train_time: 8.8986 ± 1.6062
|2025-01-30 16:29:56| Flops: 377176064
|2025-01-30 16:29:56| Params: 224658
|2025-01-30 16:29:56| Inference time: 0.19 ms
|2025-01-30 16:29:57| ********************Experiment Success********************
```

