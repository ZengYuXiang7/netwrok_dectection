```python
|2025-01-29 20:24:21| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 10, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xa39020e15b0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 20:24:21| ********************Experiment Start********************
|2025-01-29 20:25:07| Round=1 BestEpoch=174 Ac=0.8856 Pr=0.7308 Rc=0.7834 F1=0.7424 Training_time=21.4 s 

|2025-01-29 20:25:31| Round=2 BestEpoch= 79 Ac=0.8534 Pr=0.6667 Rc=0.5738 F1=0.6002 Training_time=9.5 s 

|2025-01-29 20:25:31| ********************Experiment Results:********************
|2025-01-29 20:25:31| AC: 0.8695 ± 0.0161
|2025-01-29 20:25:31| PR: 0.6988 ± 0.0320
|2025-01-29 20:25:31| RC: 0.6786 ± 0.1048
|2025-01-29 20:25:31| F1: 0.6713 ± 0.0711
|2025-01-29 20:25:31| train_time: 15.4393 ± 5.9119
|2025-01-29 20:25:31| Flops: 45061120
|2025-01-29 20:25:31| Params: 42345
|2025-01-29 20:25:31| Inference time: 0.07 ms
|2025-01-29 20:25:32| ********************Experiment Success********************
```

