```python
|2025-01-28 16:05:53| {
     'Ablation': 0, 'bs': 150, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x114fd7aabe00>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': dapp, 'num_classes': 21,
     'optim': AdamW, 'order': 2, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 50, 'record': True, 'retrain': False,
     'rounds': 2, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'try_exp': -1, 'verbose': 10,
}
|2025-01-28 16:05:53| ********************Experiment Start********************
|2025-01-28 16:20:13| Round=1 BestEpoch= 58 Ac=0.4866 Pr=0.5300 Rc=0.4135 F1=0.4292 Training_time=23.1 s 

|2025-01-28 16:20:39| Round=2 BestEpoch=  7 Ac=0.2195 Pr=0.2659 Rc=0.2756 F1=0.1476 Training_time=2.8 s 

|2025-01-28 16:20:39| ********************Experiment Results:********************
|2025-01-28 16:20:39| AC: 0.3530 ± 0.1336
|2025-01-28 16:20:39| PR: 0.3980 ± 0.1321
|2025-01-28 16:20:39| RC: 0.3446 ± 0.0690
|2025-01-28 16:20:39| F1: 0.2884 ± 0.1408
|2025-01-28 16:20:39| train_time: 12.9779 ± 10.1469
|2025-01-28 16:20:41| Flops: 104355000
|2025-01-28 16:20:41| Params: 24558
|2025-01-28 16:20:41| Inference time: 0.65 ms
|2025-01-28 16:20:41| ********************Experiment Success********************
```

