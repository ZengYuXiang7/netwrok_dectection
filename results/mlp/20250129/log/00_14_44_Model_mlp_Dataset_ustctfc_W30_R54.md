```python
|2025-01-29 00:14:44| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x136227546480>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 54, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 00:14:44| ********************Experiment Start********************
|2025-01-29 00:17:10| Round=1 BestEpoch= 12 Ac=0.6530 Pr=0.5063 Rc=0.5252 F1=0.5093 Training_time=5.6 s 

|2025-01-29 00:17:53| Round=2 BestEpoch= 45 Ac=0.6412 Pr=0.5705 Rc=0.4743 F1=0.5022 Training_time=19.7 s 

|2025-01-29 00:17:53| ********************Experiment Results:********************
|2025-01-29 00:17:53| AC: 0.6471 ± 0.0059
|2025-01-29 00:17:53| PR: 0.5384 ± 0.0321
|2025-01-29 00:17:53| RC: 0.4998 ± 0.0254
|2025-01-29 00:17:53| F1: 0.5058 ± 0.0035
|2025-01-29 00:17:53| train_time: 12.6638 ± 7.0764
|2025-01-29 00:17:53| Flops: 784384
|2025-01-29 00:17:53| Params: 6000
|2025-01-29 00:17:53| Inference time: 0.06 ms
|2025-01-29 00:17:54| ********************Experiment Success********************
```

