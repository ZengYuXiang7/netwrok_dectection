```python
|2025-01-18 01:48:01| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x5e2cb1156d0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 01:48:01| ********************Experiment Start********************
|2025-01-18 01:48:31| Acc=0.7832 F1=0.6968 Precision=0.7078 Recall=0.6904 time=1311.7 s 
|2025-01-18 01:48:31| ********************Experiment Results:********************
|2025-01-18 01:48:31| Acc: 0.7832 ± 0.0000
|2025-01-18 01:48:31| F1: 0.6968 ± 0.0000
|2025-01-18 01:48:31| P: 0.7078 ± 0.0000
|2025-01-18 01:48:31| Recall: 0.6904 ± 0.0000
|2025-01-18 01:48:31| train_time: 1311.7231 ± 0.0000
|2025-01-18 01:49:07| Flops: 2611200
|2025-01-18 01:49:07| Params: 25541
|2025-01-18 01:49:07| Inference time: 3.60 ms
|2025-01-18 01:49:07| ********************Experiment Success********************
```

