```python
|2025-01-29 20:34:47| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 10, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x95afd1ea3c0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 20:34:47| ********************Experiment Start********************
|2025-01-29 20:34:48| Ac=0.8856 Pr=0.7514 Rc=0.7680 F1=0.7522 time=20.2 s 
|2025-01-29 20:34:48| Ac=0.8622 Pr=0.7124 Rc=0.6386 F1=0.6650 time=7.7 s 
|2025-01-29 20:34:48| ********************Experiment Results:********************
|2025-01-29 20:34:48| AC: 0.8739 ± 0.0117
|2025-01-29 20:34:48| PR: 0.7319 ± 0.0195
|2025-01-29 20:34:48| RC: 0.7033 ± 0.0647
|2025-01-29 20:34:48| F1: 0.7086 ± 0.0436
|2025-01-29 20:34:48| train_time: 13.9602 ± 6.2562
|2025-01-29 20:34:48| Flops: 247010816
|2025-01-29 20:34:48| Params: 215297
|2025-01-29 20:34:48| Inference time: 0.68 ms
|2025-01-29 20:34:48| ********************Experiment Success********************
```

