```python
|2025-01-28 15:49:28| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x814b17e6cc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 15:49:28| ********************Experiment Start********************
|2025-01-28 16:04:16| Round=1 BestEpoch=113 Ac=0.7329 Pr=0.6903 Rc=0.5913 F1=0.6197 Training_time=34.2 s 

|2025-01-28 16:05:50| Round=2 BestEpoch=153 Ac=0.7309 Pr=0.6971 Rc=0.6469 F1=0.6618 Training_time=46.2 s 

|2025-01-28 16:05:50| ********************Experiment Results:********************
|2025-01-28 16:05:50| AC: 0.7319 ± 0.0010
|2025-01-28 16:05:50| PR: 0.6937 ± 0.0034
|2025-01-28 16:05:50| RC: 0.6191 ± 0.0278
|2025-01-28 16:05:50| F1: 0.6408 ± 0.0210
|2025-01-28 16:05:50| train_time: 40.2266 ± 5.9775
|2025-01-28 16:05:50| Flops: 165248
|2025-01-28 16:05:50| Params: 2524
|2025-01-28 16:05:50| Inference time: 0.03 ms
|2025-01-28 16:05:51| ********************Experiment Success********************
```

