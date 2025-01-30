```python
|2025-01-30 11:19:12| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x9abc0451c70>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-30 11:19:12| ********************Experiment Start********************
|2025-01-30 11:20:05| Round=1 BestEpoch=169 Ac=0.9477 Pr=0.6451 Rc=0.5813 F1=0.6047 Training_time=27.6 s 

|2025-01-30 11:20:49| Round=2 BestEpoch=142 Ac=0.9655 Pr=0.7578 Rc=0.7098 F1=0.7295 Training_time=23.2 s 

|2025-01-30 11:21:21| Round=3 BestEpoch= 87 Ac=0.9536 Pr=0.8091 Rc=0.6271 F1=0.6569 Training_time=14.8 s 

|2025-01-30 11:22:21| Round=4 BestEpoch=195 Ac=0.9643 Pr=0.7109 Rc=0.6719 F1=0.6684 Training_time=31.9 s 

|2025-01-30 11:22:57| Round=5 BestEpoch=107 Ac=0.9489 Pr=0.8075 Rc=0.6216 F1=0.6533 Training_time=17.6 s 

|2025-01-30 11:22:57| ********************Experiment Results:********************
|2025-01-30 11:22:57| AC: 0.9560 ± 0.0076
|2025-01-30 11:22:57| PR: 0.7461 ± 0.0622
|2025-01-30 11:22:57| RC: 0.6423 ± 0.0443
|2025-01-30 11:22:57| F1: 0.6626 ± 0.0400
|2025-01-30 11:22:57| train_time: 23.0058 ± 6.2778
|2025-01-30 11:22:57| Flops: 132710400
|2025-01-30 11:22:57| Params: 58118
|2025-01-30 11:22:57| Inference time: 0.12 ms
|2025-01-30 11:22:58| ********************Experiment Success********************
```

