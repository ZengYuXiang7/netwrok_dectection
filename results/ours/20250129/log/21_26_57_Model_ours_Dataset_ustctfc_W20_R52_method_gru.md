```python
|2025-01-29 21:26:57| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xa863512f800>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 21:26:57| ********************Experiment Start********************
|2025-01-29 21:28:23| Round=1 BestEpoch= 11 Ac=0.9159 Pr=0.5674 Rc=0.4852 F1=0.5077 Training_time=2.2 s 

|2025-01-29 21:28:59| Round=2 BestEpoch= 73 Ac=0.8770 Pr=0.5551 Rc=0.5585 F1=0.5561 Training_time=13.9 s 

|2025-01-29 21:28:59| ********************Experiment Results:********************
|2025-01-29 21:28:59| AC: 0.8964 ± 0.0194
|2025-01-29 21:28:59| PR: 0.5612 ± 0.0061
|2025-01-29 21:28:59| RC: 0.5219 ± 0.0367
|2025-01-29 21:28:59| F1: 0.5319 ± 0.0242
|2025-01-29 21:28:59| train_time: 8.0426 ± 5.8080
|2025-01-29 21:28:59| Flops: 493888512
|2025-01-29 21:28:59| Params: 429642
|2025-01-29 21:28:59| Inference time: 0.89 ms
|2025-01-29 21:29:00| ********************Experiment Success********************
```

