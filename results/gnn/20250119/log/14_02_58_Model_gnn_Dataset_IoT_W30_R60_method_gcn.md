```python
|2025-01-19 14:02:58| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x977e7df2c60>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 60, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 14:02:58| ********************Experiment Start********************
|2025-01-19 14:03:10| Acc=0.8465 F1=0.7648 Precision=0.7704 Recall=0.7621 time=833.0 s 
|2025-01-19 14:03:10| ********************Experiment Results:********************
|2025-01-19 14:03:10| Acc: 0.8465 ± 0.0000
|2025-01-19 14:03:10| F1: 0.7648 ± 0.0000
|2025-01-19 14:03:10| P: 0.7704 ± 0.0000
|2025-01-19 14:03:10| Recall: 0.7621 ± 0.0000
|2025-01-19 14:03:10| train_time: 832.9700 ± 0.0000
|2025-01-19 14:03:25| Flops: 3916800
|2025-01-19 14:03:25| Params: 38301
|2025-01-19 14:03:25| Inference time: 1.44 ms
|2025-01-19 14:03:25| ********************Experiment Success********************
```

