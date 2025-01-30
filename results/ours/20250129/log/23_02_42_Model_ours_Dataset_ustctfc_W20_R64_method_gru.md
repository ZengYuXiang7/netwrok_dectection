```python
|2025-01-29 23:02:42| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x124aa5eb0f80>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 60, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 10, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 23:02:42| ********************Experiment Start********************
|2025-01-29 23:03:32| Round=1 BestEpoch=125 Ac=0.8867 Pr=0.5108 Rc=0.4259 F1=0.4439 Training_time=23.4 s 

|2025-01-29 23:03:56| Round=2 BestEpoch= 29 Ac=0.8900 Pr=0.5366 Rc=0.5645 F1=0.5473 Training_time=5.4 s 

|2025-01-29 23:04:52| Round=3 BestEpoch=146 Ac=0.8964 Pr=0.5665 Rc=0.5420 F1=0.5501 Training_time=27.6 s 

|2025-01-29 23:05:16| Round=4 BestEpoch= 25 Ac=0.8770 Pr=0.5223 Rc=0.5118 F1=0.5145 Training_time=4.7 s 

|2025-01-29 23:06:05| Round=5 BestEpoch=124 Ac=0.8900 Pr=0.4793 Rc=0.4995 F1=0.4828 Training_time=23.2 s 

|2025-01-29 23:06:54| Round=6 BestEpoch=121 Ac=0.8803 Pr=0.5074 Rc=0.5373 F1=0.5189 Training_time=22.8 s 

|2025-01-29 23:07:23| Round=7 BestEpoch= 44 Ac=0.8479 Pr=0.4599 Rc=0.4900 F1=0.4694 Training_time=8.3 s 

|2025-01-29 23:07:54| Round=8 BestEpoch= 53 Ac=0.8641 Pr=0.4152 Rc=0.4097 F1=0.4098 Training_time=10.0 s 

|2025-01-29 23:08:19| Round=9 BestEpoch= 32 Ac=0.8608 Pr=0.4971 Rc=0.4729 F1=0.4809 Training_time=6.1 s 

|2025-01-29 23:08:56| Round=10 BestEpoch= 77 Ac=0.8964 Pr=0.5628 Rc=0.5665 F1=0.5637 Training_time=14.6 s 

|2025-01-29 23:08:56| ********************Experiment Results:********************
|2025-01-29 23:08:56| AC: 0.8790 ± 0.0156
|2025-01-29 23:08:56| PR: 0.5058 ± 0.0439
|2025-01-29 23:08:56| RC: 0.5020 ± 0.0513
|2025-01-29 23:08:56| F1: 0.4981 ± 0.0471
|2025-01-29 23:08:56| train_time: 14.6095 ± 8.3993
|2025-01-29 23:08:56| Flops: 743522304
|2025-01-29 23:08:56| Params: 648594
|2025-01-29 23:08:56| Inference time: 0.88 ms
|2025-01-29 23:08:59| ********************Experiment Success********************
```

