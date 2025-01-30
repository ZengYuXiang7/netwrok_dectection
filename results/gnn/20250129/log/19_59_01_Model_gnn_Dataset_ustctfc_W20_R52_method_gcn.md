```python
|2025-01-29 19:59:01| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x150ddc1f3f20>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 52, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 19:59:01| ********************Experiment Start********************
|2025-01-29 19:59:32| Round=1 BestEpoch= 52 Ac=0.8250 Pr=0.6315 Rc=0.5906 F1=0.5965 Training_time=10.1 s 

|2025-01-29 19:59:32| ********************Experiment Results:********************
|2025-01-29 19:59:32| AC: 0.8250 ± 0.0000
|2025-01-29 19:59:32| PR: 0.6315 ± 0.0000
|2025-01-29 19:59:32| RC: 0.5906 ± 0.0000
|2025-01-29 19:59:32| F1: 0.5965 ± 0.0000
|2025-01-29 19:59:32| train_time: 10.0619 ± 0.0000
|2025-01-29 19:59:33| Flops: 1996800
|2025-01-29 19:59:33| Params: 18113
|2025-01-29 19:59:33| Inference time: 1.26 ms
|2025-01-29 19:59:33| ********************Experiment Success********************
```

