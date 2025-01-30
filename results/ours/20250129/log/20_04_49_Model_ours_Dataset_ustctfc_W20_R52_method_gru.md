```python
|2025-01-29 20:04:49| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x107b4bf4f7a0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 20:04:49| ********************Experiment Start********************
|2025-01-29 20:04:50| Ac=0.8550 Pr=0.7602 Rc=0.7742 F1=0.7620 time=12.9 s 
|2025-01-29 20:04:50| Ac=0.8400 Pr=0.7638 Rc=0.5910 F1=0.6387 time=9.0 s 
|2025-01-29 20:04:50| ********************Experiment Results:********************
|2025-01-29 20:04:50| AC: 0.8475 ± 0.0075
|2025-01-29 20:04:50| PR: 0.7620 ± 0.0018
|2025-01-29 20:04:50| RC: 0.6826 ± 0.0916
|2025-01-29 20:04:50| F1: 0.7003 ± 0.0616
|2025-01-29 20:04:50| train_time: 10.9795 ± 1.9680
|2025-01-29 20:04:50| Flops: 493881856
|2025-01-29 20:04:50| Params: 429589
|2025-01-29 20:04:50| Inference time: 1.11 ms
|2025-01-29 20:04:50| ********************Experiment Success********************
```

