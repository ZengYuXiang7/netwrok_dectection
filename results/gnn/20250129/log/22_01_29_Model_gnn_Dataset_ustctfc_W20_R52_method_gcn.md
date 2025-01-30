```python
|2025-01-29 22:01:29| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xe6536d14c80>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 52, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 22:01:29| ********************Experiment Start********************
|2025-01-29 22:01:30| Ac=0.8479 Pr=0.4703 Rc=0.4428 F1=0.4531 time=12.9 s 
|2025-01-29 22:01:30| ********************Experiment Results:********************
|2025-01-29 22:01:30| AC: 0.8479 ± 0.0000
|2025-01-29 22:01:30| PR: 0.4703 ± 0.0000
|2025-01-29 22:01:30| RC: 0.4428 ± 0.0000
|2025-01-29 22:01:30| F1: 0.4531 ± 0.0000
|2025-01-29 22:01:30| train_time: 12.9100 ± 0.0000
|2025-01-29 22:01:31| Flops: 2063360
|2025-01-29 22:01:31| Params: 19154
|2025-01-29 22:01:31| Inference time: 1.34 ms
