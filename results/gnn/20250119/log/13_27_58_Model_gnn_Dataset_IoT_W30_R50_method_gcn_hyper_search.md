```python
|2025-01-19 13:27:58| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x73dbcece4ec0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 13:27:58| ********************Experiment Start********************
|2025-01-19 13:44:13| Round=1 BestEpoch=226 Acc=0.8616 F1=0.7862 Precision=0.7960 Recall=0.7802 Training_time=738.5 s 

|2025-01-19 13:44:13| ********************Experiment Results:********************
|2025-01-19 13:44:13| Acc: 0.8616 ± 0.0000
|2025-01-19 13:44:13| F1: 0.7862 ± 0.0000
|2025-01-19 13:44:13| P: 0.7960 ± 0.0000
|2025-01-19 13:44:13| Recall: 0.7802 ± 0.0000
|2025-01-19 13:44:13| train_time: 738.4636 ± 0.0000
|2025-01-19 13:44:28| Flops: 3264000
|2025-01-19 13:44:28| Params: 31921
|2025-01-19 13:44:28| Inference time: 1.22 ms
|2025-01-19 13:44:28| ********************Experiment Success********************
```

