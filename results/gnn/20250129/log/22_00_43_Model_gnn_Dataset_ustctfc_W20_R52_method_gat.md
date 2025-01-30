```python
|2025-01-29 22:00:43| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0xd9a66894f50>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 22:00:43| ********************Experiment Start********************
|2025-01-29 22:00:44| Ac=0.8576 Pr=0.4817 Rc=0.4463 F1=0.4594 time=25.7 s 
|2025-01-29 22:00:44| ********************Experiment Results:********************
|2025-01-29 22:00:44| AC: 0.8576 ± 0.0000
|2025-01-29 22:00:44| PR: 0.4817 ± 0.0000
|2025-01-29 22:00:44| RC: 0.4463 ± 0.0000
|2025-01-29 22:00:44| F1: 0.4594 ± 0.0000
|2025-01-29 22:00:44| train_time: 25.7062 ± 0.0000
|2025-01-29 22:00:45| Flops: 22830080
|2025-01-29 22:00:45| Params: 35378
|2025-01-29 22:00:45| Inference time: 1.69 ms
