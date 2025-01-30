```python
|2025-01-30 16:29:59| {
     'ablation': 3, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x78c050a0fb00>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 60, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-30 16:29:59| ********************Experiment Start********************
|2025-01-30 16:30:34| Round=1 BestEpoch=124 Ac=0.8770 Pr=0.5035 Rc=0.4549 F1=0.4712 Training_time=14.5 s 

|2025-01-30 16:31:03| Round=2 BestEpoch= 95 Ac=0.8641 Pr=0.5174 Rc=0.4410 F1=0.4603 Training_time=11.0 s 

|2025-01-30 16:31:03| ********************Experiment Results:********************
|2025-01-30 16:31:03| AC: 0.8706 ± 0.0065
|2025-01-30 16:31:03| PR: 0.5104 ± 0.0070
|2025-01-30 16:31:03| RC: 0.4479 ± 0.0069
|2025-01-30 16:31:03| F1: 0.4657 ± 0.0055
|2025-01-30 16:31:03| train_time: 12.7679 ± 1.7443
|2025-01-30 16:31:03| Flops: 75874304
|2025-01-30 16:31:03| Params: 92370
|2025-01-30 16:31:03| Inference time: 0.35 ms
|2025-01-30 16:31:03| ********************Experiment Success********************
```

