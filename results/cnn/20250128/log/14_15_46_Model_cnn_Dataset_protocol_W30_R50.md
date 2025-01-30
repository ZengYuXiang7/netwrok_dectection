```python
|2025-01-28 14:15:46| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x10d77a58ecc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 14:15:46| ********************Experiment Start********************
|2025-01-28 14:16:13| Round=1 BestEpoch= 95 Ac=0.3598 Pr=0.2421 Rc=0.2243 F1=0.2171 Training_time=11.1 s 

|2025-01-28 14:16:46| Round=2 BestEpoch=130 Ac=0.4533 Pr=0.4366 Rc=0.3374 F1=0.3400 Training_time=15.0 s 

|2025-01-28 14:16:46| ********************Experiment Results:********************
|2025-01-28 14:16:46| AC: 0.4065 ± 0.0467
|2025-01-28 14:16:46| PR: 0.3394 ± 0.0972
|2025-01-28 14:16:46| RC: 0.2809 ± 0.0565
|2025-01-28 14:16:46| F1: 0.2785 ± 0.0614
|2025-01-28 14:16:46| train_time: 13.0374 ± 1.9195
|2025-01-28 14:16:47| Flops: 31283200
|2025-01-28 14:16:47| Params: 9327
|2025-01-28 14:16:47| Inference time: 0.10 ms
|2025-01-28 14:16:47| ********************Experiment Success********************
```

