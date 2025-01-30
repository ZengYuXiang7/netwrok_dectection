```python
|2025-01-28 16:20:44| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x151c9760a240>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.0025, 'model': graphiot, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 16:20:44| ********************Experiment Start********************
|2025-01-28 16:22:17| Round=1 BestEpoch=111 Ac=0.5909 Pr=0.6666 Rc=0.5949 F1=0.6103 Training_time=55.1 s 

|2025-01-28 16:24:09| Round=2 BestEpoch=129 Ac=0.6614 Pr=0.6856 Rc=0.5715 F1=0.5948 Training_time=69.7 s 

|2025-01-28 16:24:09| ********************Experiment Results:********************
|2025-01-28 16:24:09| AC: 0.6261 ± 0.0353
|2025-01-28 16:24:09| PR: 0.6761 ± 0.0095
|2025-01-28 16:24:09| RC: 0.5832 ± 0.0117
|2025-01-28 16:24:09| F1: 0.6026 ± 0.0078
|2025-01-28 16:24:09| train_time: 62.3912 ± 7.3380
|2025-01-28 16:24:11| Flops: 46828800
|2025-01-28 16:24:11| Params: 25158
|2025-01-28 16:24:11| Inference time: 0.87 ms
|2025-01-28 16:24:12| ********************Experiment Success********************
```

