```python
|2025-01-29 21:34:53| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xe0d27cfa480>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 2, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 52, 'record': True,
     'retrain': False, 'rounds': 2, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 21:34:53| ********************Experiment Start********************
|2025-01-29 21:35:11| Round=1 BestEpoch= 35 Ac=0.8479 Pr=0.4739 Rc=0.4414 F1=0.4531 Training_time=5.8 s 

|2025-01-29 21:35:53| Round=2 BestEpoch=118 Ac=0.8738 Pr=0.5017 Rc=0.4530 F1=0.4689 Training_time=20.2 s 

|2025-01-29 21:35:53| ********************Experiment Results:********************
|2025-01-29 21:35:53| AC: 0.8608 ± 0.0129
|2025-01-29 21:35:53| PR: 0.4878 ± 0.0139
|2025-01-29 21:35:53| RC: 0.4472 ± 0.0058
|2025-01-29 21:35:53| F1: 0.4610 ± 0.0079
|2025-01-29 21:35:53| train_time: 13.0078 ± 7.2289
|2025-01-29 21:35:54| Flops: 4992000
|2025-01-29 21:35:54| Params: 21702
|2025-01-29 21:35:54| Inference time: 0.24 ms
|2025-01-29 21:35:54| ********************Experiment Success********************
```

