```python
|2025-01-11 08:08:07| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x1122f86ba4e0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 6, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 08:08:07| ********************Experiment Start********************
|2025-01-11 08:08:26| Acc=0.8041 F1=0.7234 Precision=0.7387 Recall=0.7132 time=1506.3 s 
|2025-01-11 08:08:26| ********************Experiment Results:********************
|2025-01-11 08:08:26| Acc: 0.8041 ± 0.0000
|2025-01-11 08:08:26| F1: 0.7234 ± 0.0000
|2025-01-11 08:08:26| P: 0.7387 ± 0.0000
|2025-01-11 08:08:26| Recall: 0.7132 ± 0.0000
|2025-01-11 08:08:26| train_time: 1506.2758 ± 0.0000
|2025-01-11 08:08:49| Flops: 25231360
|2025-01-11 08:08:49| Params: 70805
|2025-01-11 08:08:49| Inference time: 0.36 ms
|2025-01-11 08:08:49| ********************Experiment Success********************
```

