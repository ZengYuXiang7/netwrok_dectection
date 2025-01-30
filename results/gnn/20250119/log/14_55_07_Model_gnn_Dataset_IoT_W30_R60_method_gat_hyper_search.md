```python
|2025-01-19 14:55:07| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x73fd76e07950>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 60,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 14:55:07| ********************Experiment Start********************
|2025-01-19 15:14:53| Round=1 BestEpoch=197 Acc=0.8932 F1=0.8271 Precision=0.8342 Recall=0.8243 Training_time=910.1 s 

|2025-01-19 15:14:53| ********************Experiment Results:********************
|2025-01-19 15:14:53| Acc: 0.8932 ± 0.0000
|2025-01-19 15:14:53| F1: 0.8271 ± 0.0000
|2025-01-19 15:14:53| P: 0.8342 ± 0.0000
|2025-01-19 15:14:53| Recall: 0.8243 ± 0.0000
|2025-01-19 15:14:53| train_time: 910.1100 ± 0.0000
|2025-01-19 15:15:09| Flops: 45388800
|2025-01-19 15:15:09| Params: 59901
|2025-01-19 15:15:09| Inference time: 1.53 ms
|2025-01-19 15:15:09| ********************Experiment Success********************
```

