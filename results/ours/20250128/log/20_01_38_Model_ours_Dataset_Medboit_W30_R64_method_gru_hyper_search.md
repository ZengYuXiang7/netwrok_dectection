```python
|2025-01-28 20:01:38| {
     'ablation': 3, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': Medboit, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x789ab7a7bb00>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-28 20:01:38| ********************Experiment Start********************
|2025-01-28 20:03:37| Round=1 BestEpoch=284 Ac=0.7299 Pr=0.6810 Rc=0.6274 F1=0.6445 Training_time=70.6 s 

|2025-01-28 20:04:29| Round=2 BestEpoch= 97 Ac=0.7269 Pr=0.6769 Rc=0.6759 F1=0.6744 Training_time=24.2 s 

|2025-01-28 20:04:29| ********************Experiment Results:********************
|2025-01-28 20:04:29| AC: 0.7284 ± 0.0015
|2025-01-28 20:04:29| PR: 0.6789 ± 0.0020
|2025-01-28 20:04:29| RC: 0.6517 ± 0.0243
|2025-01-28 20:04:29| F1: 0.6594 ± 0.0150
|2025-01-28 20:04:29| train_time: 47.4023 ± 23.2367
|2025-01-28 20:04:29| Flops: 113639424
|2025-01-28 20:04:29| Params: 116680
|2025-01-28 20:04:29| Inference time: 0.42 ms
|2025-01-28 20:04:30| ********************Experiment Success********************
```

