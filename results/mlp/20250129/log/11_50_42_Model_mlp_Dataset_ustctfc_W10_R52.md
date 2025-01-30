```python
|2025-01-29 11:50:42| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 10, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x12b873c03bc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 11:50:42| ********************Experiment Start********************
|2025-01-29 11:51:35| Round=1 BestEpoch= 46 Ac=0.6005 Pr=0.5945 Rc=0.5906 F1=0.5708 Training_time=24.6 s 

|2025-01-29 11:53:00| Round=2 BestEpoch= 91 Ac=0.5964 Pr=0.5365 Rc=0.5044 F1=0.5026 Training_time=49.6 s 

|2025-01-29 11:53:00| ********************Experiment Results:********************
|2025-01-29 11:53:00| AC: 0.5985 ± 0.0021
|2025-01-29 11:53:00| PR: 0.5655 ± 0.0290
|2025-01-29 11:53:00| RC: 0.5475 ± 0.0431
|2025-01-29 11:53:00| F1: 0.5367 ± 0.0341
|2025-01-29 11:53:00| train_time: 37.0624 ± 12.5095
|2025-01-29 11:53:00| Flops: 609280
|2025-01-29 11:53:00| Params: 4636
|2025-01-29 11:53:00| Inference time: 0.06 ms
|2025-01-29 11:53:01| ********************Experiment Success********************
```

