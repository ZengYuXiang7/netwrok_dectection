```python
|2025-01-29 19:54:40| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xe8b0feaa3c0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 19:54:40| ********************Experiment Start********************
|2025-01-29 19:54:53| Round=1 BestEpoch= 38 Ac=0.8150 Pr=0.6560 Rc=0.5745 F1=0.6024 Training_time=4.1 s 

|2025-01-29 19:55:01| Round=2 BestEpoch= 13 Ac=0.8250 Pr=0.7267 Rc=0.5197 F1=0.5769 Training_time=1.3 s 

|2025-01-29 19:55:01| ********************Experiment Results:********************
|2025-01-29 19:55:01| AC: 0.8200 ± 0.0050
|2025-01-29 19:55:01| PR: 0.6914 ± 0.0354
|2025-01-29 19:55:01| RC: 0.5471 ± 0.0274
|2025-01-29 19:55:01| F1: 0.5896 ± 0.0127
|2025-01-29 19:55:01| train_time: 2.6940 ± 1.3732
|2025-01-29 19:55:01| Flops: 654336
|2025-01-29 19:55:01| Params: 4991
|2025-01-29 19:55:01| Inference time: 0.06 ms
