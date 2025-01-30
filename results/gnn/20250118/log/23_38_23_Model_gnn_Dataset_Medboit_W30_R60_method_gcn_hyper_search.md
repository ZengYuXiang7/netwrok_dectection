```python
|2025-01-18 23:38:23| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x78d85aa57b00>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 60, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 23:38:23| ********************Experiment Start********************
|2025-01-18 23:42:14| Round=1 BestEpoch= 94 Acc=0.9385 F1=0.7275 Precision=0.7371 Recall=0.7217 Training_time=146.0 s 

|2025-01-18 23:42:14| ********************Experiment Results:********************
|2025-01-18 23:42:14| Acc: 0.9385 ± 0.0000
|2025-01-18 23:42:14| F1: 0.7275 ± 0.0000
|2025-01-18 23:42:14| P: 0.7371 ± 0.0000
|2025-01-18 23:42:14| Recall: 0.7217 ± 0.0000
|2025-01-18 23:42:14| train_time: 146.0490 ± 0.0000
|2025-01-18 23:42:22| Flops: 2419200
|2025-01-18 23:42:22| Params: 14888
|2025-01-18 23:42:22| Inference time: 1.22 ms
|2025-01-18 23:42:22| ********************Experiment Success********************
```

