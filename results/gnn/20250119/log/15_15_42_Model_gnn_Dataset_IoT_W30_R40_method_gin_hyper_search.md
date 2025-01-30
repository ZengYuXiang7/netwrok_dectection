```python
|2025-01-19 15:15:42| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gin, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x79fd6d9f8140>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 15:15:42| ********************Experiment Start********************
|2025-01-19 15:38:05| Round=1 BestEpoch=498 Acc=0.8365 F1=0.7587 Precision=0.7708 Recall=0.7545 Training_time=1111.5 s 

|2025-01-19 15:38:05| ********************Experiment Results:********************
|2025-01-19 15:38:05| Acc: 0.8365 ± 0.0000
|2025-01-19 15:38:05| F1: 0.7587 ± 0.0000
|2025-01-19 15:38:05| P: 0.7708 ± 0.0000
|2025-01-19 15:38:05| Recall: 0.7545 ± 0.0000
|2025-01-19 15:38:05| train_time: 1111.5454 ± 0.0000
|2025-01-19 15:38:20| Flops: 5068800
|2025-01-19 15:38:20| Params: 27021
|2025-01-19 15:38:20| Inference time: 0.30 ms
|2025-01-19 15:38:21| ********************Experiment Success********************
```

