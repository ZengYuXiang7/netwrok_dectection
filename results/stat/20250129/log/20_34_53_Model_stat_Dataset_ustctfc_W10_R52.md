```python
|2025-01-29 20:34:53| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 10, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xbace1a081d0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 20:34:53| ********************Experiment Start********************
|2025-01-29 20:34:54| Ac=0.7185 Pr=0.6815 Rc=0.4954 F1=0.5194 time=12.4 s 
|2025-01-29 20:34:54| Ac=0.7126 Pr=0.6126 Rc=0.4456 F1=0.4705 time=15.0 s 
|2025-01-29 20:34:54| ********************Experiment Results:********************
|2025-01-29 20:34:54| AC: 0.7155 ± 0.0029
|2025-01-29 20:34:54| PR: 0.6471 ± 0.0344
|2025-01-29 20:34:54| RC: 0.4705 ± 0.0249
|2025-01-29 20:34:54| F1: 0.4949 ± 0.0244
|2025-01-29 20:34:54| train_time: 13.6626 ± 1.2934
|2025-01-29 20:34:54| Flops: 204032
|2025-01-29 20:34:54| Params: 3119
|2025-01-29 20:34:54| Inference time: 0.04 ms
|2025-01-29 20:34:54| ********************Experiment Success********************
```

