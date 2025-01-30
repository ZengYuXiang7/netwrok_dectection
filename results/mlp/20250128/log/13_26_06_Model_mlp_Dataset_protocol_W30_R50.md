```python
|2025-01-28 13:26:06| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x62abb335430>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 13:26:06| ********************Experiment Start********************
|2025-01-28 13:32:00| Round=1 BestEpoch= 59 Ac=0.6188 Pr=0.6331 Rc=0.5822 F1=0.5942 Training_time=6.8 s 

|2025-01-28 13:32:27| Round=2 BestEpoch=100 Ac=0.6485 Pr=0.7378 Rc=0.6918 F1=0.6961 Training_time=11.3 s 

|2025-01-28 13:32:27| ********************Experiment Results:********************
|2025-01-28 13:32:27| AC: 0.6337 ± 0.0149
|2025-01-28 13:32:27| PR: 0.6854 ± 0.0523
|2025-01-28 13:32:27| RC: 0.6370 ± 0.0548
|2025-01-28 13:32:27| F1: 0.6452 ± 0.0509
|2025-01-28 13:32:27| train_time: 9.0439 ± 2.2295
|2025-01-28 13:32:27| Flops: 646144
|2025-01-28 13:32:27| Params: 4936
|2025-01-28 13:32:27| Inference time: 0.06 ms
|2025-01-28 13:32:28| ********************Experiment Success********************
```

