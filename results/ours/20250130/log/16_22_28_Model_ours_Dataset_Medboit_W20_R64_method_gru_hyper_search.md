```python
|2025-01-30 16:22:28| {
     'ablation': 3, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': Medboit, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x78be7736cbf0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 60, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-30 16:22:28| ********************Experiment Start********************
|2025-01-30 16:24:40| Round=1 BestEpoch=411 Ac=0.9655 Pr=0.7371 Rc=0.7039 F1=0.7140 Training_time=79.0 s 

|2025-01-30 16:26:30| Round=2 BestEpoch=375 Ac=0.9536 Pr=0.6471 Rc=0.6305 F1=0.6380 Training_time=66.0 s 

|2025-01-30 16:26:30| ********************Experiment Results:********************
|2025-01-30 16:26:30| AC: 0.9596 ± 0.0059
|2025-01-30 16:26:30| PR: 0.6921 ± 0.0450
|2025-01-30 16:26:30| RC: 0.6672 ± 0.0367
|2025-01-30 16:26:30| F1: 0.6760 ± 0.0380
|2025-01-30 16:26:30| train_time: 72.4823 ± 6.5122
|2025-01-30 16:26:30| Flops: 75776000
|2025-01-30 16:26:30| Params: 91590
|2025-01-30 16:26:30| Inference time: 0.36 ms
|2025-01-30 16:26:31| ********************Experiment Success********************
```

