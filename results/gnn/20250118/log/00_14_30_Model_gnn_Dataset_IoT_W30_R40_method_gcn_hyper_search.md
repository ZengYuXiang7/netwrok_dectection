```python
|2025-01-18 00:14:30| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x768b439c6d80>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 00:14:30| ********************Experiment Start********************
|2025-01-18 00:47:58| Round=1 BestEpoch=370 Acc=0.8192 F1=0.7389 Precision=0.7539 Recall=0.7307 Training_time=1311.7 s 

|2025-01-18 00:47:58| ********************Experiment Results:********************
|2025-01-18 00:47:58| Acc: 0.8192 ± 0.0000
|2025-01-18 00:47:58| F1: 0.7389 ± 0.0000
|2025-01-18 00:47:58| P: 0.7539 ± 0.0000
|2025-01-18 00:47:58| Recall: 0.7307 ± 0.0000
|2025-01-18 00:47:58| train_time: 1311.7231 ± 0.0000
|2025-01-18 00:48:14| Flops: 2611200
|2025-01-18 00:48:14| Params: 25541
|2025-01-18 00:48:14| Inference time: 1.23 ms
|2025-01-18 00:48:14| ********************Experiment Success********************
```

