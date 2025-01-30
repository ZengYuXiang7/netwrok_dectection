```python
|2025-01-29 22:00:12| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x936f0b9f320>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 22:00:12| ********************Experiment Start********************
|2025-01-29 22:00:12| Ac=0.8803 Pr=0.4589 Rc=0.4542 F1=0.4501 time=16.0 s 
|2025-01-29 22:00:12| Ac=0.8803 Pr=0.5372 Rc=0.5278 F1=0.5268 time=13.1 s 
|2025-01-29 22:00:12| ********************Experiment Results:********************
|2025-01-29 22:00:12| AC: 0.8803 ± 0.0000
|2025-01-29 22:00:12| PR: 0.4981 ± 0.0392
|2025-01-29 22:00:12| RC: 0.4910 ± 0.0368
|2025-01-29 22:00:12| F1: 0.4885 ± 0.0384
|2025-01-29 22:00:12| train_time: 14.5454 ± 1.4944
|2025-01-29 22:00:12| Flops: 90255360
|2025-01-29 22:00:12| Params: 52226
|2025-01-29 22:00:12| Inference time: 0.08 ms
