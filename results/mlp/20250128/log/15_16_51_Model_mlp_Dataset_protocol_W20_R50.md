```python
|2025-01-28 15:16:51| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x153ca239a300>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 15:16:51| ********************Experiment Start********************
|2025-01-28 15:22:45| Round=1 BestEpoch= 25 Ac=0.6168 Pr=0.6485 Rc=0.5803 F1=0.6026 Training_time=3.3 s 

|2025-01-28 15:23:18| Round=2 BestEpoch=105 Ac=0.6533 Pr=0.6590 Rc=0.6078 F1=0.6238 Training_time=13.2 s 

|2025-01-28 15:23:18| ********************Experiment Results:********************
|2025-01-28 15:23:18| AC: 0.6350 ± 0.0182
|2025-01-28 15:23:18| PR: 0.6537 ± 0.0053
|2025-01-28 15:23:18| RC: 0.5940 ± 0.0138
|2025-01-28 15:23:18| F1: 0.6132 ± 0.0106
|2025-01-28 15:23:18| train_time: 8.2491 ± 4.9772
|2025-01-28 15:23:18| Flops: 582144
|2025-01-28 15:23:18| Params: 4436
|2025-01-28 15:23:18| Inference time: 0.06 ms
|2025-01-28 15:23:19| ********************Experiment Success********************
```

