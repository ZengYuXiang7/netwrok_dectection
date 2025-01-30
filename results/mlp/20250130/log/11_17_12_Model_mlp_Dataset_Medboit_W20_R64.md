```python
|2025-01-30 11:17:12| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x9396c367110>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-30 11:17:12| ********************Experiment Start********************
|2025-01-30 11:17:55| Round=1 BestEpoch=142 Ac=0.9548 Pr=0.6889 Rc=0.6369 F1=0.6535 Training_time=21.3 s 

|2025-01-30 11:18:25| Round=2 BestEpoch= 93 Ac=0.9144 Pr=0.6191 Rc=0.4014 F1=0.4317 Training_time=13.8 s 

|2025-01-30 11:18:40| Round=3 BestEpoch= 31 Ac=0.8989 Pr=0.4546 Rc=0.3907 F1=0.4060 Training_time=4.6 s 

|2025-01-30 11:18:54| Round=4 BestEpoch= 26 Ac=0.8847 Pr=0.6342 Rc=0.3840 F1=0.4235 Training_time=4.0 s 

|2025-01-30 11:19:08| Round=5 BestEpoch= 23 Ac=0.9144 Pr=0.6199 Rc=0.5262 F1=0.5573 Training_time=3.8 s 

|2025-01-30 11:19:08| ********************Experiment Results:********************
|2025-01-30 11:19:08| AC: 0.9134 ± 0.0235
|2025-01-30 11:19:08| PR: 0.6033 ± 0.0786
|2025-01-30 11:19:08| RC: 0.4678 ± 0.0994
|2025-01-30 11:19:08| F1: 0.4944 ± 0.0959
|2025-01-30 11:19:08| train_time: 9.4910 ± 6.9879
|2025-01-30 11:19:08| Flops: 805888
|2025-01-30 11:19:08| Params: 6162
|2025-01-30 11:19:08| Inference time: 0.06 ms
|2025-01-30 11:19:09| ********************Experiment Success********************
```

