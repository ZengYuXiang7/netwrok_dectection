```python
|2025-01-29 21:50:13| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xa728a64ea80>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 21:50:13| ********************Experiment Start********************
|2025-01-29 21:50:14| Ac=0.8608 Pr=0.4990 Rc=0.4468 F1=0.4641 time=1.9 s 
|2025-01-29 21:50:14| Ac=0.8252 Pr=0.5354 Rc=0.4472 F1=0.4723 time=2.7 s 
|2025-01-29 21:50:14| ********************Experiment Results:********************
|2025-01-29 21:50:14| AC: 0.8430 ± 0.0178
|2025-01-29 21:50:14| PR: 0.5172 ± 0.0182
|2025-01-29 21:50:14| RC: 0.4470 ± 0.0002
|2025-01-29 21:50:14| F1: 0.4682 ± 0.0041
|2025-01-29 21:50:14| train_time: 2.3009 ± 0.4274
|2025-01-29 21:50:14| Flops: 661504
|2025-01-29 21:50:14| Params: 5046
|2025-01-29 21:50:14| Inference time: 0.07 ms
|2025-01-29 21:50:14| ********************Experiment Success********************
```

