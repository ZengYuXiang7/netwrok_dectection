```python
|2025-01-18 01:49:12| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x745c090aaa20>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 40,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 01:49:12| ********************Experiment Start********************
|2025-01-18 02:37:46| Round=1 BestEpoch=141 Acc=0.8318 F1=0.7443 Precision=0.7583 Recall=0.7395 Training_time=2142.0 s 

|2025-01-18 02:37:46| ********************Experiment Results:********************
|2025-01-18 02:37:46| Acc: 0.8318 ± 0.0000
|2025-01-18 02:37:46| F1: 0.7443 ± 0.0000
|2025-01-18 02:37:46| P: 0.7583 ± 0.0000
|2025-01-18 02:37:46| Recall: 0.7395 ± 0.0000
|2025-01-18 02:37:46| train_time: 2141.9560 ± 0.0000
|2025-01-18 02:38:21| Flops: 21043200
|2025-01-18 02:38:21| Params: 35141
|2025-01-18 02:38:21| Inference time: 3.71 ms
|2025-01-18 02:38:22| ********************Experiment Success********************
```

