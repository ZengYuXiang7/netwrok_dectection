```python
|2025-01-29 20:40:11| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xe88570af3b0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 20:40:11| ********************Experiment Start********************
|2025-01-29 20:40:12| Ac=0.8600 Pr=0.7362 Rc=0.7796 F1=0.7490 time=12.9 s 
|2025-01-29 20:40:12| Ac=0.8400 Pr=0.7638 Rc=0.5910 F1=0.6387 time=9.0 s 
|2025-01-29 20:40:12| ********************Experiment Results:********************
|2025-01-29 20:40:12| AC: 0.8500 ± 0.0100
|2025-01-29 20:40:12| PR: 0.7500 ± 0.0138
|2025-01-29 20:40:12| RC: 0.6853 ± 0.0943
|2025-01-29 20:40:12| F1: 0.6938 ± 0.0552
|2025-01-29 20:40:12| train_time: 10.9795 ± 1.9680
|2025-01-29 20:40:12| Flops: 493881856
|2025-01-29 20:40:12| Params: 429589
|2025-01-29 20:40:12| Inference time: 1.10 ms
|2025-01-29 20:40:12| ********************Experiment Success********************
```

