```python
|2025-01-19 06:07:59| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x79153c696de0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 40,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 06:07:59| ********************Experiment Start********************
|2025-01-19 06:10:35| Round=1 BestEpoch=168 Acc=0.7418 F1=0.6800 Precision=0.6869 Recall=0.6768 Training_time=104.7 s 

|2025-01-19 06:10:35| ********************Experiment Results:********************
|2025-01-19 06:10:35| Acc: 0.7418 ± 0.0000
|2025-01-19 06:10:35| F1: 0.6800 ± 0.0000
|2025-01-19 06:10:35| P: 0.6869 ± 0.0000
|2025-01-19 06:10:35| Recall: 0.6768 ± 0.0000
|2025-01-19 06:10:35| train_time: 104.7241 ± 0.0000
|2025-01-19 06:10:37| Flops: 20044800
|2025-01-19 06:10:37| Params: 19528
|2025-01-19 06:10:37| Inference time: 1.42 ms
|2025-01-19 06:10:37| ********************Experiment Success********************
```

