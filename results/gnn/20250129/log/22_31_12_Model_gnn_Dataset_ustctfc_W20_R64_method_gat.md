```python
|2025-01-29 22:31:12| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0xdcef8dfef30>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 5, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 22:31:12| ********************Experiment Start********************
|2025-01-29 22:32:01| Round=1 BestEpoch=104 Ac=0.8867 Pr=0.4717 Rc=0.4899 F1=0.4707 Training_time=26.1 s 

|2025-01-29 22:32:57| Round=2 BestEpoch=111 Ac=0.8447 Pr=0.4936 Rc=0.4658 F1=0.4762 Training_time=29.6 s 

|2025-01-29 22:34:02| Round=3 BestEpoch=122 Ac=0.8641 Pr=0.4840 Rc=0.4492 F1=0.4622 Training_time=36.2 s 

|2025-01-29 22:34:37| Round=4 BestEpoch= 49 Ac=0.8738 Pr=0.4877 Rc=0.4534 F1=0.4663 Training_time=14.5 s 

|2025-01-29 22:35:27| Round=5 BestEpoch= 95 Ac=0.8738 Pr=0.5039 Rc=0.4534 F1=0.4701 Training_time=26.5 s 

|2025-01-29 22:35:27| ********************Experiment Results:********************
|2025-01-29 22:35:27| AC: 0.8686 ± 0.0140
|2025-01-29 22:35:27| PR: 0.4882 ± 0.0106
|2025-01-29 22:35:27| RC: 0.4623 ± 0.0149
|2025-01-29 22:35:27| F1: 0.4691 ± 0.0047
|2025-01-29 22:35:27| train_time: 26.5909 ± 7.0308
|2025-01-29 22:35:28| Flops: 33996800
|2025-01-29 22:35:28| Params: 48146
|2025-01-29 22:35:28| Inference time: 1.44 ms
|2025-01-29 22:35:29| ********************Experiment Success********************
```

