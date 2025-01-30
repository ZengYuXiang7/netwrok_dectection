```python
|2025-01-29 23:31:05| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gat, 'heads': 2, 'hyper_search': False,
     'log': <utils.logger.Logger object at 0xfe2266947a0>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 10, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 23:31:05| ********************Experiment Start********************
|2025-01-29 23:31:58| Round=1 BestEpoch=104 Ac=0.8867 Pr=0.4717 Rc=0.4899 F1=0.4707 Training_time=28.7 s 

|2025-01-29 23:32:57| Round=2 BestEpoch=111 Ac=0.8447 Pr=0.4936 Rc=0.4658 F1=0.4762 Training_time=32.1 s 

|2025-01-29 23:34:01| Round=3 BestEpoch=122 Ac=0.8641 Pr=0.4840 Rc=0.4492 F1=0.4622 Training_time=35.8 s 

|2025-01-29 23:34:35| Round=4 BestEpoch= 49 Ac=0.8738 Pr=0.4877 Rc=0.4534 F1=0.4663 Training_time=14.4 s 

|2025-01-29 23:35:28| Round=5 BestEpoch= 95 Ac=0.8738 Pr=0.5039 Rc=0.4534 F1=0.4701 Training_time=27.7 s 

|2025-01-29 23:36:18| Round=6 BestEpoch= 86 Ac=0.8835 Pr=0.5187 Rc=0.5045 F1=0.5061 Training_time=25.7 s 

|2025-01-29 23:37:34| Round=7 BestEpoch=150 Ac=0.8770 Pr=0.5046 Rc=0.4549 F1=0.4716 Training_time=44.4 s 

|2025-01-29 23:38:16| Round=8 BestEpoch= 67 Ac=0.8770 Pr=0.5063 Rc=0.4780 F1=0.4878 Training_time=19.8 s 

|2025-01-29 23:39:07| Round=9 BestEpoch= 89 Ac=0.8867 Pr=0.5097 Rc=0.4819 F1=0.4912 Training_time=26.4 s 

|2025-01-29 23:39:59| Round=10 BestEpoch= 90 Ac=0.8641 Pr=0.5000 Rc=0.4818 F1=0.4866 Training_time=27.0 s 

|2025-01-29 23:39:59| ********************Experiment Results:********************
|2025-01-29 23:39:59| AC: 0.8731 ± 0.0122
|2025-01-29 23:39:59| PR: 0.4980 ± 0.0132
|2025-01-29 23:39:59| RC: 0.4713 ± 0.0177
|2025-01-29 23:39:59| F1: 0.4789 ± 0.0129
|2025-01-29 23:39:59| train_time: 28.2066 ± 7.7968
|2025-01-29 23:39:59| Flops: 33996800
|2025-01-29 23:39:59| Params: 48146
|2025-01-29 23:39:59| Inference time: 1.61 ms
|2025-01-29 23:40:02| ********************Experiment Success********************
```

