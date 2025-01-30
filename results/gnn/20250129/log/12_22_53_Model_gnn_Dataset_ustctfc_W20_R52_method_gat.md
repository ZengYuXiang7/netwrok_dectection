```python
|2025-01-29 12:22:53| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0x6976113b0e0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 12:22:53| ********************Experiment Start********************
|2025-01-29 12:30:30| Round=1 BestEpoch= 76 Ac=0.6150 Pr=0.5181 Rc=0.5366 F1=0.5180 Training_time=283.9 s 

|2025-01-29 12:30:30| ********************Experiment Results:********************
|2025-01-29 12:30:30| AC: 0.6150 ± 0.0000
|2025-01-29 12:30:30| PR: 0.5181 ± 0.0000
|2025-01-29 12:30:30| RC: 0.5366 ± 0.0000
|2025-01-29 12:30:30| F1: 0.5180 ± 0.0000
|2025-01-29 12:30:30| train_time: 283.8828 ± 0.0000
|2025-01-29 12:30:42| Flops: 22963200
|2025-01-29 12:30:42| Params: 37460
|2025-01-29 12:30:42| Inference time: 1.59 ms
|2025-01-29 12:30:42| ********************Experiment Success********************
```

