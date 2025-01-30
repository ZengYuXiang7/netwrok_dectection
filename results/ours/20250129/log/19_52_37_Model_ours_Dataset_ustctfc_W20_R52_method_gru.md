```python
|2025-01-29 19:52:37| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x15070dd332c0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 19:52:37| ********************Experiment Start********************
|2025-01-29 19:54:08| Round=1 BestEpoch= 74 Ac=0.8500 Pr=0.7576 Rc=0.7707 F1=0.7584 Training_time=12.9 s 

|2025-01-29 19:54:36| Round=2 BestEpoch= 52 Ac=0.8300 Pr=0.7547 Rc=0.6181 F1=0.6497 Training_time=9.0 s 

|2025-01-29 19:54:36| ********************Experiment Results:********************
|2025-01-29 19:54:36| AC: 0.8400 ± 0.0100
|2025-01-29 19:54:36| PR: 0.7561 ± 0.0015
|2025-01-29 19:54:36| RC: 0.6944 ± 0.0763
|2025-01-29 19:54:36| F1: 0.7040 ± 0.0543
|2025-01-29 19:54:36| train_time: 10.9795 ± 1.9680
|2025-01-29 19:54:37| Flops: 493881856
|2025-01-29 19:54:37| Params: 429589
|2025-01-29 19:54:37| Inference time: 0.86 ms
|2025-01-29 19:54:37| ********************Experiment Success********************
```

