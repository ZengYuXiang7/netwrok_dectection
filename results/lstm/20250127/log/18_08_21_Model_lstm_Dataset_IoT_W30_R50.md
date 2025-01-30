```python
|2025-01-27 18:08:21| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x12138b4d49e0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-27 18:08:21| ********************Experiment Start********************
|2025-01-27 18:10:36| Round=1 BestEpoch=143 Ac=0.8918 Pr=0.8329 Rc=0.8280 F1=0.8296   Training_time=91.4 s 

|2025-01-27 18:13:32| Round=2 BestEpoch=204 Ac=0.8970 Pr=0.8476 Rc=0.8398 F1=0.8423   Training_time=123.8 s 

|2025-01-27 18:13:32| ********************Experiment Results:********************
|2025-01-27 18:13:32| AC: 0.8944 ± 0.0026
|2025-01-27 18:13:32| PR: 0.8402 ± 0.0073
|2025-01-27 18:13:32| RC: 0.8339 ± 0.0059
|2025-01-27 18:13:32| F1: 0.8360 ± 0.0063
|2025-01-27 18:13:32| train_time: 107.6347 ± 16.1938
|2025-01-27 18:13:32| Flops: 126144000
|2025-01-27 18:13:32| Params: 62521
|2025-01-27 18:13:32| Inference time: 0.07 ms
|2025-01-27 18:13:32| ********************Experiment Success********************
```

