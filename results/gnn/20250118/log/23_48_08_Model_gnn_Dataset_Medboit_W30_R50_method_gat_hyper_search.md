```python
|2025-01-18 23:48:08| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x791e81046fc0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 23:48:08| ********************Experiment Start********************
|2025-01-18 23:54:10| Round=1 BestEpoch=122 Acc=0.9390 F1=0.7393 Precision=0.7512 Recall=0.7284 Training_time=253.5 s 

|2025-01-18 23:54:10| ********************Experiment Results:********************
|2025-01-18 23:54:10| Acc: 0.9390 ± 0.0000
|2025-01-18 23:54:10| F1: 0.7393 ± 0.0000
|2025-01-18 23:54:10| P: 0.7512 ± 0.0000
|2025-01-18 23:54:10| Recall: 0.7284 ± 0.0000
|2025-01-18 23:54:10| train_time: 253.4791 ± 0.0000
|2025-01-18 23:54:17| Flops: 30816000
|2025-01-18 23:54:17| Params: 27408
|2025-01-18 23:54:17| Inference time: 1.43 ms
|2025-01-18 23:54:17| ********************Experiment Success********************
```

