```python
|2025-01-29 22:16:21| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x12599980a300>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 60, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 22:16:21| ********************Experiment Start********************
|2025-01-29 22:17:12| Round=1 BestEpoch=125 Ac=0.8867 Pr=0.5108 Rc=0.4259 F1=0.4439 Training_time=23.7 s 

|2025-01-29 22:17:35| Round=2 BestEpoch= 29 Ac=0.8900 Pr=0.5366 Rc=0.5645 F1=0.5473 Training_time=5.1 s 

|2025-01-29 22:18:28| Round=3 BestEpoch=146 Ac=0.8964 Pr=0.5665 Rc=0.5420 F1=0.5501 Training_time=26.1 s 

|2025-01-29 22:18:50| Round=4 BestEpoch= 25 Ac=0.8770 Pr=0.5223 Rc=0.5118 F1=0.5145 Training_time=4.4 s 

|2025-01-29 22:19:38| Round=5 BestEpoch=124 Ac=0.8900 Pr=0.4793 Rc=0.4995 F1=0.4828 Training_time=22.1 s 

|2025-01-29 22:19:38| ********************Experiment Results:********************
|2025-01-29 22:19:38| AC: 0.8880 ± 0.0063
|2025-01-29 22:19:38| PR: 0.5231 ± 0.0288
|2025-01-29 22:19:38| RC: 0.5087 ± 0.0473
|2025-01-29 22:19:38| F1: 0.5077 ± 0.0402
|2025-01-29 22:19:38| train_time: 16.2801 ± 9.4899
|2025-01-29 22:19:38| Flops: 743522304
|2025-01-29 22:19:38| Params: 648594
|2025-01-29 22:19:38| Inference time: 0.89 ms
|2025-01-29 22:19:39| ********************Experiment Success********************
```

