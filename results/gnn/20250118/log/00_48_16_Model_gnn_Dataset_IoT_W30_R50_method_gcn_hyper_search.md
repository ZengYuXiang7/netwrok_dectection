```python
|2025-01-18 00:48:16| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c0ecc25b860>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 00:48:16| ********************Experiment Start********************
|2025-01-18 01:01:38| Round=1 BestEpoch=173 Acc=0.8027 F1=0.7169 Precision=0.7342 Recall=0.7067 Training_time=573.7 s 

|2025-01-18 01:01:38| ********************Experiment Results:********************
|2025-01-18 01:01:38| Acc: 0.8027 ± 0.0000
|2025-01-18 01:01:38| F1: 0.7169 ± 0.0000
|2025-01-18 01:01:38| P: 0.7342 ± 0.0000
|2025-01-18 01:01:38| Recall: 0.7067 ± 0.0000
|2025-01-18 01:01:38| train_time: 573.7341 ± 0.0000
|2025-01-18 01:01:54| Flops: 3264000
|2025-01-18 01:01:54| Params: 31921
|2025-01-18 01:01:54| Inference time: 1.31 ms
|2025-01-18 01:01:54| ********************Experiment Success********************
```

