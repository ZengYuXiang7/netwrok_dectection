```python
|2025-01-18 04:26:36| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0x1448a20aecc0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 04:26:36| ********************Experiment Start********************
|2025-01-18 04:27:06| Acc=0.8198 F1=0.7374 Precision=0.7491 Recall=0.7306 time=1946.5 s 
|2025-01-18 04:27:06| ********************Experiment Results:********************
|2025-01-18 04:27:06| Acc: 0.8198 ± 0.0000
|2025-01-18 04:27:06| F1: 0.7374 ± 0.0000
|2025-01-18 04:27:06| P: 0.7491 ± 0.0000
|2025-01-18 04:27:06| Recall: 0.7306 ± 0.0000
|2025-01-18 04:27:06| train_time: 1946.4805 ± 0.0000
|2025-01-18 04:27:42| Flops: 32064000
|2025-01-18 04:27:42| Params: 46921
|2025-01-18 04:27:42| Inference time: 4.86 ms
|2025-01-18 04:27:42| ********************Experiment Success********************
```

