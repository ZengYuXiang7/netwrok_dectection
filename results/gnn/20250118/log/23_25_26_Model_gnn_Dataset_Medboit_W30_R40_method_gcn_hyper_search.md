```python
|2025-01-18 23:25:26| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x79b862aaa480>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 23:25:26| ********************Experiment Start********************
|2025-01-18 23:32:46| Round=1 BestEpoch=204 Acc=0.9377 F1=0.7367 Precision=0.7489 Recall=0.7258 Training_time=325.2 s 

|2025-01-18 23:32:46| ********************Experiment Results:********************
|2025-01-18 23:32:46| Acc: 0.9377 ± 0.0000
|2025-01-18 23:32:46| F1: 0.7367 ± 0.0000
|2025-01-18 23:32:46| P: 0.7489 ± 0.0000
|2025-01-18 23:32:46| Recall: 0.7258 ± 0.0000
|2025-01-18 23:32:46| train_time: 325.1964 ± 0.0000
|2025-01-18 23:32:53| Flops: 1612800
|2025-01-18 23:32:53| Params: 9928
|2025-01-18 23:32:53| Inference time: 1.23 ms
|2025-01-18 23:32:53| ********************Experiment Success********************
```

