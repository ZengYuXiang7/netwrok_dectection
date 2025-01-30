```python
|2025-01-28 13:36:59| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xae71bbaa090>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 2, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 2, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-28 13:36:59| ********************Experiment Start********************
|2025-01-28 13:37:00| Ac=0.5842 Pr=0.6194 Rc=0.5839 F1=0.5973 time=9.1 s 
|2025-01-28 13:37:01| Ac=0.5594 Pr=0.5871 Rc=0.5518 F1=0.5629 time=9.9 s 
|2025-01-28 13:37:01| ********************Experiment Results:********************
|2025-01-28 13:37:01| AC: 0.5718 ± 0.0124
|2025-01-28 13:37:01| PR: 0.6032 ± 0.0162
|2025-01-28 13:37:01| RC: 0.5679 ± 0.0161
|2025-01-28 13:37:01| F1: 0.5801 ± 0.0172
|2025-01-28 13:37:01| train_time: 9.5099 ± 0.3669
|2025-01-28 13:37:01| Flops: 6432000
|2025-01-28 13:37:01| Params: 20762
|2025-01-28 13:37:01| Inference time: 0.28 ms
|2025-01-28 13:37:01| ********************Experiment Success********************
```

