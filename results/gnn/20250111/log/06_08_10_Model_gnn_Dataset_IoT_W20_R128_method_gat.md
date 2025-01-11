```python
|2025-01-11 06:08:10| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0xa9064da4800>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 6, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 128,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 06:08:10| ********************Experiment Start********************
|2025-01-11 06:08:29| Acc=0.8760 F1=0.8152 Precision=0.8193 Recall=0.8127 time=1605.5 s 
|2025-01-11 06:08:29| ********************Experiment Results:********************
|2025-01-11 06:08:29| Acc: 0.8760 ± 0.0000
|2025-01-11 06:08:29| F1: 0.8152 ± 0.0000
|2025-01-11 06:08:29| P: 0.8193 ± 0.0000
|2025-01-11 06:08:29| Recall: 0.8127 ± 0.0000
|2025-01-11 06:08:29| train_time: 1605.5470 ± 0.0000
|2025-01-11 06:08:53| Flops: 131399680
|2025-01-11 06:08:53| Params: 153109
|2025-01-11 06:08:53| Inference time: 1.82 ms
|2025-01-11 06:08:53| ********************Experiment Success********************
```

