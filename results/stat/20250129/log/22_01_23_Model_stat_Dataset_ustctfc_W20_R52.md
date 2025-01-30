```python
|2025-01-29 22:01:23| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x10da1c13d730>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 22:01:23| ********************Experiment Start********************
|2025-01-29 22:01:23| Ac=0.6246 Pr=0.3089 Rc=0.2821 F1=0.2831 time=6.4 s 
|2025-01-29 22:01:23| Ac=0.6084 Pr=0.2752 Rc=0.2472 F1=0.2487 time=10.1 s 
|2025-01-29 22:01:23| ********************Experiment Results:********************
|2025-01-29 22:01:23| AC: 0.6165 ± 0.0081
|2025-01-29 22:01:23| PR: 0.2921 ± 0.0168
|2025-01-29 22:01:23| RC: 0.2646 ± 0.0175
|2025-01-29 22:01:23| F1: 0.2659 ± 0.0172
|2025-01-29 22:01:23| train_time: 8.2839 ± 1.8573
|2025-01-29 22:01:23| Flops: 207616
|2025-01-29 22:01:23| Params: 3174
|2025-01-29 22:01:23| Inference time: 0.05 ms
