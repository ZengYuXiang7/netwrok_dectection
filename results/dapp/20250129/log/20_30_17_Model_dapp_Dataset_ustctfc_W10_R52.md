```python
|2025-01-29 20:30:17| {
     'ablation': 0, 'bs': 150, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 10, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x69aaa48ecc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': dapp, 'num_classes': 21,
     'optim': AdamW, 'order': 2, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 52, 'record': True, 'retrain': False,
     'rounds': 2, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'try_exp': -1, 'verbose': 10,
}
|2025-01-29 20:30:17| ********************Experiment Start********************
|2025-01-29 20:30:56| Round=1 BestEpoch= 98 Ac=0.8182 Pr=0.5050 Rc=0.4841 F1=0.4911 Training_time=17.1 s 

|2025-01-29 20:31:31| Round=2 BestEpoch= 81 Ac=0.8651 Pr=0.7143 Rc=0.7169 F1=0.7020 Training_time=14.3 s 

|2025-01-29 20:31:31| ********************Experiment Results:********************
|2025-01-29 20:31:31| AC: 0.8416 ± 0.0235
|2025-01-29 20:31:31| PR: 0.6096 ± 0.1046
|2025-01-29 20:31:31| RC: 0.6005 ± 0.1164
|2025-01-29 20:31:31| F1: 0.5966 ± 0.1054
|2025-01-29 20:31:31| train_time: 15.6763 ± 1.4052
|2025-01-29 20:31:31| Flops: 37915800
|2025-01-29 20:31:31| Params: 27889
|2025-01-29 20:31:31| Inference time: 0.66 ms
|2025-01-29 20:31:32| ********************Experiment Success********************
```

