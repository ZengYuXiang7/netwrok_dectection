```python
|2025-01-29 21:33:20| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xd0a82aa0d40>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 52, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 21:33:20| ********************Experiment Start********************
|2025-01-29 21:33:57| Round=1 BestEpoch= 58 Ac=0.8738 Pr=0.4954 Rc=0.4765 F1=0.4818 Training_time=12.9 s 

|2025-01-29 21:33:57| ********************Experiment Results:********************
|2025-01-29 21:33:57| AC: 0.8738 ± 0.0000
|2025-01-29 21:33:57| PR: 0.4954 ± 0.0000
|2025-01-29 21:33:57| RC: 0.4765 ± 0.0000
|2025-01-29 21:33:57| F1: 0.4818 ± 0.0000
|2025-01-29 21:33:57| train_time: 12.9100 ± 0.0000
|2025-01-29 21:33:57| Flops: 2063360
|2025-01-29 21:33:57| Params: 19154
|2025-01-29 21:33:57| Inference time: 1.25 ms
|2025-01-29 21:33:58| ********************Experiment Success********************
```

