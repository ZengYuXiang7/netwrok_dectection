```python
|2025-01-29 22:09:05| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x6c96de672c0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 22:09:05| ********************Experiment Start********************
|2025-01-29 22:09:06| Ac=0.8964 Pr=0.4649 Rc=0.4293 F1=0.4407 time=2.2 s 
|2025-01-29 22:09:06| Ac=0.8123 Pr=0.4298 Rc=0.3665 F1=0.3752 time=13.9 s 
|2025-01-29 22:09:33| Round=3 BestEpoch= 48 Ac=0.8867 Pr=0.5607 Rc=0.5153 F1=0.5274 Training_time=9.1 s 

|2025-01-29 22:10:06| Round=4 BestEpoch= 69 Ac=0.8900 Pr=0.5610 Rc=0.5406 F1=0.5473 Training_time=13.1 s 

|2025-01-29 22:10:49| Round=5 BestEpoch=102 Ac=0.8770 Pr=0.5600 Rc=0.4940 F1=0.5097 Training_time=20.2 s 

|2025-01-29 22:10:49| ********************Experiment Results:********************
|2025-01-29 22:10:49| AC: 0.8725 ± 0.0307
|2025-01-29 22:10:49| PR: 0.5153 ± 0.0566
|2025-01-29 22:10:49| RC: 0.4691 ± 0.0632
|2025-01-29 22:10:49| F1: 0.4801 ± 0.0635
|2025-01-29 22:10:49| train_time: 11.6852 ± 5.9160
|2025-01-29 22:10:49| Flops: 493888512
|2025-01-29 22:10:49| Params: 429642
|2025-01-29 22:10:49| Inference time: 0.87 ms
|2025-01-29 22:10:49| ********************Experiment Success********************
```

