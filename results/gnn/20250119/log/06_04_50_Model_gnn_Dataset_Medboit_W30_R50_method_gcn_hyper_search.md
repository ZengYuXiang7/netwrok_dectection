```python
|2025-01-19 06:04:50| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x771f7f9c0d40>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 06:04:50| ********************Experiment Start********************
|2025-01-19 06:05:46| Round=1 BestEpoch= 57 Acc=0.7358 F1=0.6433 Precision=0.6958 Recall=0.6204 Training_time=27.7 s 

|2025-01-19 06:05:46| ********************Experiment Results:********************
|2025-01-19 06:05:46| Acc: 0.7358 ± 0.0000
|2025-01-19 06:05:46| F1: 0.6433 ± 0.0000
|2025-01-19 06:05:46| P: 0.6958 ± 0.0000
|2025-01-19 06:05:46| Recall: 0.6204 ± 0.0000
|2025-01-19 06:05:46| train_time: 27.6681 ± 0.0000
|2025-01-19 06:05:48| Flops: 2016000
|2025-01-19 06:05:48| Params: 12408
|2025-01-19 06:05:48| Inference time: 1.17 ms
|2025-01-19 06:05:49| ********************Experiment Success********************
```

