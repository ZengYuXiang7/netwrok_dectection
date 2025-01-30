```python
|2025-01-19 03:29:58| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7bfc8bf4fec0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 03:29:58| ********************Experiment Start********************
|2025-01-19 03:46:15| Round=1 BestEpoch=226 Acc=0.8616 F1=0.7862 Precision=0.7960 Recall=0.7802 Training_time=740.5 s 

|2025-01-19 03:46:15| ********************Experiment Results:********************
|2025-01-19 03:46:15| Acc: 0.8616 ± 0.0000
|2025-01-19 03:46:15| F1: 0.7862 ± 0.0000
|2025-01-19 03:46:15| P: 0.7960 ± 0.0000
|2025-01-19 03:46:15| Recall: 0.7802 ± 0.0000
|2025-01-19 03:46:15| train_time: 740.5061 ± 0.0000
|2025-01-19 03:46:30| Flops: 3264000
|2025-01-19 03:46:30| Params: 31921
|2025-01-19 03:46:30| Inference time: 1.21 ms
|2025-01-19 03:46:31| ********************Experiment Success********************
```

