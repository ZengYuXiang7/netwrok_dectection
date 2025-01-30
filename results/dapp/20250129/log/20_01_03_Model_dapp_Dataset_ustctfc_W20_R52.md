```python
|2025-01-29 20:01:03| {
     'ablation': 0, 'bs': 150, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x108d89a28d70>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': dapp, 'num_classes': 21,
     'optim': AdamW, 'order': 2, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 52, 'record': True, 'retrain': False,
     'rounds': 2, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'try_exp': -1, 'verbose': 10,
}
|2025-01-29 20:01:03| ********************Experiment Start********************
|2025-01-29 20:01:24| Round=1 BestEpoch= 45 Ac=0.8000 Pr=0.5264 Rc=0.4169 F1=0.4324 Training_time=6.7 s 

|2025-01-29 20:01:57| Round=2 BestEpoch= 84 Ac=0.8400 Pr=0.7168 Rc=0.6194 F1=0.6149 Training_time=12.8 s 

|2025-01-29 20:01:57| ********************Experiment Results:********************
|2025-01-29 20:01:57| AC: 0.8200 ± 0.0200
|2025-01-29 20:01:57| PR: 0.6216 ± 0.0952
|2025-01-29 20:01:57| RC: 0.5181 ± 0.1013
|2025-01-29 20:01:57| F1: 0.5236 ± 0.0913
|2025-01-29 20:01:57| train_time: 9.7676 ± 3.0536
|2025-01-29 20:01:57| Flops: 75433800
|2025-01-29 20:01:57| Params: 27889
|2025-01-29 20:01:57| Inference time: 0.67 ms
|2025-01-29 20:01:58| ********************Experiment Success********************
```

