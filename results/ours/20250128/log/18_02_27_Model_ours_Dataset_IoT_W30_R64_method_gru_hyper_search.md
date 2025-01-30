```python
|2025-01-28 18:02:27| {
     'ablation': 1, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7117d01b2420>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-28 18:02:27| ********************Experiment Start********************
|2025-01-28 18:04:39| Round=1 BestEpoch=155 Ac=0.5135 Pr=0.4262 Rc=0.3406 F1=0.3524 Training_time=78.6 s 

|2025-01-28 18:06:59| Round=2 BestEpoch=179 Ac=0.5079 Pr=0.4506 Rc=0.3398 F1=0.3548 Training_time=85.6 s 

|2025-01-28 18:06:59| ********************Experiment Results:********************
|2025-01-28 18:06:59| AC: 0.5107 ± 0.0028
|2025-01-28 18:06:59| PR: 0.4384 ± 0.0122
|2025-01-28 18:06:59| RC: 0.3402 ± 0.0004
|2025-01-28 18:06:59| F1: 0.3536 ± 0.0012
|2025-01-28 18:06:59| train_time: 82.0868 ± 3.5294
|2025-01-28 18:07:00| Flops: 450560
|2025-01-28 18:07:00| Params: 3477
|2025-01-28 18:07:00| Inference time: 0.02 ms
|2025-01-28 18:07:00| ********************Experiment Success********************
```

