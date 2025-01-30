```python
|2025-01-28 15:10:05| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xce86dbc60f0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 15:10:05| ********************Experiment Start********************
|2025-01-28 15:16:16| Round=1 BestEpoch= 52 Ac=0.5693 Pr=0.6383 Rc=0.4455 F1=0.4658 Training_time=7.5 s 

|2025-01-28 15:16:48| Round=2 BestEpoch= 93 Ac=0.6168 Pr=0.5239 Rc=0.4515 F1=0.4663 Training_time=13.2 s 

|2025-01-28 15:16:48| ********************Experiment Results:********************
|2025-01-28 15:16:48| AC: 0.5931 ± 0.0237
|2025-01-28 15:16:48| PR: 0.5811 ± 0.0572
|2025-01-28 15:16:48| RC: 0.4485 ± 0.0030
|2025-01-28 15:16:48| F1: 0.4661 ± 0.0003
|2025-01-28 15:16:48| train_time: 10.3556 ± 2.8370
|2025-01-28 15:16:48| Flops: 179072
|2025-01-28 15:16:48| Params: 2736
|2025-01-28 15:16:48| Inference time: 0.04 ms
|2025-01-28 15:16:48| ********************Experiment Success********************
```

