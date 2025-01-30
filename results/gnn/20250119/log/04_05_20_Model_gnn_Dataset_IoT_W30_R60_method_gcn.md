```python
|2025-01-19 04:05:20| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xb4ac9ef7740>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 60, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 04:05:20| ********************Experiment Start********************
|2025-01-19 04:05:32| Acc=0.8465 F1=0.7648 Precision=0.7704 Recall=0.7621 time=857.2 s 
|2025-01-19 04:05:32| ********************Experiment Results:********************
|2025-01-19 04:05:32| Acc: 0.8465 ± 0.0000
|2025-01-19 04:05:32| F1: 0.7648 ± 0.0000
|2025-01-19 04:05:32| P: 0.7704 ± 0.0000
|2025-01-19 04:05:32| Recall: 0.7621 ± 0.0000
|2025-01-19 04:05:32| train_time: 857.2219 ± 0.0000
|2025-01-19 04:05:47| Flops: 3916800
|2025-01-19 04:05:47| Params: 38301
|2025-01-19 04:05:47| Inference time: 1.35 ms
|2025-01-19 04:05:47| ********************Experiment Success********************
```

