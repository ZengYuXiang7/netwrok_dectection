```python
|2025-01-19 06:14:32| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0xcb2a0292c00>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 06:14:32| ********************Experiment Start********************
|2025-01-19 06:14:34| Acc=0.7408 F1=0.6603 Precision=0.6941 Recall=0.6423 time=77.6 s 
|2025-01-19 06:14:34| ********************Experiment Results:********************
|2025-01-19 06:14:34| Acc: 0.7408 ± 0.0000
|2025-01-19 06:14:34| F1: 0.6603 ± 0.0000
|2025-01-19 06:14:34| P: 0.6941 ± 0.0000
|2025-01-19 06:14:34| Recall: 0.6423 ± 0.0000
|2025-01-19 06:14:34| train_time: 77.5583 ± 0.0000
|2025-01-19 06:14:36| Flops: 30816000
|2025-01-19 06:14:36| Params: 27408
|2025-01-19 06:14:36| Inference time: 1.64 ms
|2025-01-19 06:14:36| ********************Experiment Success********************
```

