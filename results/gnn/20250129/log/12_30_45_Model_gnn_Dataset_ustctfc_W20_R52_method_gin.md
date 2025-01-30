```python
|2025-01-29 12:30:45| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xbb457b57110>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 2, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 52, 'record': True,
     'retrain': False, 'rounds': 2, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 12:30:45| ********************Experiment Start********************
|2025-01-29 12:33:25| Round=1 BestEpoch= 43 Ac=0.6102 Pr=0.3657 Rc=0.3643 F1=0.3561 Training_time=74.0 s 

|2025-01-29 12:37:41| Round=2 BestEpoch= 79 Ac=0.6061 Pr=0.3799 Rc=0.3784 F1=0.3662 Training_time=146.8 s 

|2025-01-29 12:37:41| ********************Experiment Results:********************
|2025-01-29 12:37:41| AC: 0.6081 ± 0.0020
|2025-01-29 12:37:41| PR: 0.3728 ± 0.0071
|2025-01-29 12:37:41| RC: 0.3714 ± 0.0070
|2025-01-29 12:37:41| F1: 0.3611 ± 0.0050
|2025-01-29 12:37:41| train_time: 110.3839 ± 36.4148
|2025-01-29 12:37:54| Flops: 5125120
|2025-01-29 12:37:54| Params: 23784
|2025-01-29 12:37:54| Inference time: 0.26 ms
|2025-01-29 12:37:54| ********************Experiment Success********************
```

