```python
|2025-01-29 00:38:43| {
     'ablation': 0, 'bs': 150, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xdce23a9f110>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': dapp, 'num_classes': 21,
     'optim': AdamW, 'order': 2, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 54, 'record': True, 'retrain': False,
     'rounds': 2, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'try_exp': -1, 'verbose': 10,
}
|2025-01-29 00:38:43| ********************Experiment Start********************
|2025-01-29 00:42:04| Round=1 BestEpoch= 96 Ac=0.6185 Pr=0.5910 Rc=0.5739 F1=0.5436 Training_time=116.3 s 

|2025-01-29 00:45:31| Round=2 BestEpoch= 99 Ac=0.6166 Pr=0.5549 Rc=0.5898 F1=0.5540 Training_time=123.1 s 

|2025-01-29 00:45:31| ********************Experiment Results:********************
|2025-01-29 00:45:31| AC: 0.6176 ± 0.0010
|2025-01-29 00:45:31| PR: 0.5730 ± 0.0181
|2025-01-29 00:45:31| RC: 0.5819 ± 0.0080
|2025-01-29 00:45:31| F1: 0.5488 ± 0.0052
|2025-01-29 00:45:31| train_time: 119.7231 ± 3.4135
|2025-01-29 00:45:42| Flops: 121743000
|2025-01-29 00:45:42| Params: 30422
|2025-01-29 00:45:42| Inference time: 0.71 ms
|2025-01-29 00:45:43| ********************Experiment Success********************
```

