```python
|2025-01-29 20:43:12| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x6c141c26fc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 20:43:12| ********************Experiment Start********************
|2025-01-29 20:43:26| Round=1 BestEpoch= 54 Ac=0.8641 Pr=0.4986 Rc=0.4495 F1=0.4654 Training_time=4.9 s 

|2025-01-29 20:43:37| Round=2 BestEpoch= 32 Ac=0.8447 Pr=0.5406 Rc=0.5204 F1=0.5283 Training_time=2.8 s 

|2025-01-29 20:43:37| ********************Experiment Results:********************
|2025-01-29 20:43:37| AC: 0.8544 ± 0.0097
|2025-01-29 20:43:37| PR: 0.5196 ± 0.0210
|2025-01-29 20:43:37| RC: 0.4849 ± 0.0355
|2025-01-29 20:43:37| F1: 0.4968 ± 0.0315
|2025-01-29 20:43:37| train_time: 3.8875 ± 1.0513
|2025-01-29 20:43:37| Flops: 661504
|2025-01-29 20:43:37| Params: 5046
|2025-01-29 20:43:37| Inference time: 0.06 ms
|2025-01-29 20:43:37| ********************Experiment Success********************
```

