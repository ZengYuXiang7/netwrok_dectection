```python
|2025-01-28 15:37:14| {
     'Ablation': 0, 'bs': 150, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x12197fb76ff0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': dapp, 'num_classes': 21,
     'optim': AdamW, 'order': 2, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 50, 'record': True, 'retrain': False,
     'rounds': 2, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'try_exp': -1, 'verbose': 10,
}
|2025-01-28 15:37:14| ********************Experiment Start********************
|2025-01-28 15:38:00| Round=1 BestEpoch=150 Ac=0.5730 Pr=0.5714 Rc=0.5549 F1=0.5448 Training_time=22.0 s 

|2025-01-28 15:38:15| Round=2 BestEpoch= 25 Ac=0.5036 Pr=0.6066 Rc=0.4601 F1=0.4979 Training_time=3.9 s 

|2025-01-28 15:38:15| ********************Experiment Results:********************
|2025-01-28 15:38:15| AC: 0.5383 ± 0.0347
|2025-01-28 15:38:15| PR: 0.5890 ± 0.0176
|2025-01-28 15:38:15| RC: 0.5075 ± 0.0474
|2025-01-28 15:38:15| F1: 0.5214 ± 0.0235
|2025-01-28 15:38:15| train_time: 12.9181 ± 9.0581
|2025-01-28 15:38:16| Flops: 69720000
|2025-01-28 15:38:16| Params: 25162
|2025-01-28 15:38:16| Inference time: 0.66 ms
|2025-01-28 15:38:16| ********************Experiment Success********************
```

