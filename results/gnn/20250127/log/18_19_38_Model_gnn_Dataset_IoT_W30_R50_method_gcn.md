```python
|2025-01-27 18:19:38| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xb09db1e8050>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-27 18:19:38| ********************Experiment Start********************
|2025-01-27 18:40:31| Round=1 BestEpoch=226 Ac=0.8616 Pr=0.7960 Rc=0.7802 F1=0.7862   Training_time=762.6 s 

|2025-01-27 18:40:31| ********************Experiment Results:********************
|2025-01-27 18:40:31| AC: 0.8616 ± 0.0000
|2025-01-27 18:40:31| PR: 0.7960 ± 0.0000
|2025-01-27 18:40:31| RC: 0.7802 ± 0.0000
|2025-01-27 18:40:31| F1: 0.7862 ± 0.0000
|2025-01-27 18:40:31| train_time: 762.5551 ± 0.0000
|2025-01-27 18:40:45| Flops: 3264000
|2025-01-27 18:40:45| Params: 31921
|2025-01-27 18:40:45| Inference time: 1.21 ms
|2025-01-27 18:40:46| ********************Experiment Success********************
```

