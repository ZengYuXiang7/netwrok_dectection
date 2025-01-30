```python
|2025-01-29 20:13:45| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x144de913d160>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 20:13:45| ********************Experiment Start********************
|2025-01-29 20:15:20| Round=1 BestEpoch= 93 Ac=0.8421 Pr=0.6246 Rc=0.5851 F1=0.5964 Training_time=15.1 s 

|2025-01-29 20:15:49| Round=2 BestEpoch= 57 Ac=0.7970 Pr=0.6365 Rc=0.5623 F1=0.5653 Training_time=9.3 s 

|2025-01-29 20:15:49| ********************Experiment Results:********************
|2025-01-29 20:15:49| AC: 0.8195 ± 0.0226
|2025-01-29 20:15:49| PR: 0.6305 ± 0.0059
|2025-01-29 20:15:49| RC: 0.5737 ± 0.0114
|2025-01-29 20:15:49| F1: 0.5808 ± 0.0155
|2025-01-29 20:15:49| train_time: 12.2131 ± 2.9248
|2025-01-29 20:15:49| Flops: 740752896
|2025-01-29 20:15:49| Params: 643881
|2025-01-29 20:15:49| Inference time: 1.21 ms
|2025-01-29 20:15:50| ********************Experiment Success********************
```

