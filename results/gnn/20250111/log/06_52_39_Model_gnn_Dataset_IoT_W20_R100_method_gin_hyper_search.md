```python
|2025-01-11 06:52:39| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7f667a8feff0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 6, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 100, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 06:52:39| ********************Experiment Start********************
|2025-01-11 07:35:12| Round=1 BestEpoch=477 Acc=0.8175 F1=0.7421 Precision=0.7646 Recall=0.7280 Training_time=2069.6 s 

|2025-01-11 07:35:12| ********************Experiment Results:********************
|2025-01-11 07:35:12| Acc: 0.8175 ± 0.0000
|2025-01-11 07:35:12| F1: 0.7421 ± 0.0000
|2025-01-11 07:35:12| P: 0.7646 ± 0.0000
|2025-01-11 07:35:12| Recall: 0.7280 ± 0.0000
|2025-01-11 07:35:12| train_time: 2069.5886 ± 0.0000
|2025-01-11 07:35:37| Flops: 16128000
|2025-01-11 07:35:37| Params: 52521
|2025-01-11 07:35:37| Inference time: 0.28 ms
|2025-01-11 07:35:37| ********************Experiment Success********************
```

