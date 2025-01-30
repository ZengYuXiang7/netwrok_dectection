```python
|2025-01-29 20:36:28| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 10, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x570d692be00>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 20:36:28| ********************Experiment Start********************
|2025-01-29 20:36:29| Ac=0.8768 Pr=0.7478 Rc=0.7485 F1=0.7397 time=7.6 s 
|2025-01-29 20:36:29| Ac=0.8387 Pr=0.6623 Rc=0.6166 F1=0.6325 time=12.2 s 
|2025-01-29 20:36:29| ********************Experiment Results:********************
|2025-01-29 20:36:29| AC: 0.8578 ± 0.0191
|2025-01-29 20:36:29| PR: 0.7050 ± 0.0428
|2025-01-29 20:36:29| RC: 0.6826 ± 0.0660
|2025-01-29 20:36:29| F1: 0.6861 ± 0.0536
|2025-01-29 20:36:29| train_time: 9.8676 ± 2.2902
|2025-01-29 20:36:29| Flops: 587776
|2025-01-29 20:36:29| Params: 4471
|2025-01-29 20:36:29| Inference time: 0.07 ms
|2025-01-29 20:36:29| ********************Experiment Success********************
```

