```python
|2025-01-29 22:01:26| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xe43adf77860>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 22:01:26| ********************Experiment Start********************
|2025-01-29 22:01:26| Ac=0.8350 Pr=0.4669 Rc=0.4383 F1=0.4483 time=14.3 s 
|2025-01-29 22:01:26| Ac=0.8026 Pr=0.3280 Rc=0.3391 F1=0.3324 time=6.0 s 
|2025-01-29 22:01:26| ********************Experiment Results:********************
|2025-01-29 22:01:26| AC: 0.8188 ± 0.0162
|2025-01-29 22:01:26| PR: 0.3974 ± 0.0695
|2025-01-29 22:01:26| RC: 0.3887 ± 0.0496
|2025-01-29 22:01:26| F1: 0.3904 ± 0.0580
|2025-01-29 22:01:26| train_time: 10.1869 ± 4.1553
|2025-01-29 22:01:27| Flops: 22490624
|2025-01-29 22:01:27| Params: 9534
|2025-01-29 22:01:27| Inference time: 0.11 ms
