```python
|2025-01-27 18:13:35| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x8f3505bf6e0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-27 18:13:35| ********************Experiment Start********************
|2025-01-27 18:15:55| Round=1 BestEpoch=157 Ac=0.8590 Pr=0.8122 Rc=0.7856 F1=0.7800   Training_time=92.2 s 

|2025-01-27 18:19:35| Round=2 BestEpoch=266 Ac=0.8796 Pr=0.8487 Rc=0.8109 F1=0.8143   Training_time=156.0 s 

|2025-01-27 18:19:35| ********************Experiment Results:********************
|2025-01-27 18:19:35| AC: 0.8693 ± 0.0103
|2025-01-27 18:19:35| PR: 0.8305 ± 0.0183
|2025-01-27 18:19:35| RC: 0.7982 ± 0.0127
|2025-01-27 18:19:35| F1: 0.7971 ± 0.0172
|2025-01-27 18:19:35| train_time: 124.1265 ± 31.8938
|2025-01-27 18:19:35| Flops: 31244800
|2025-01-27 18:19:35| Params: 9021
|2025-01-27 18:19:35| Inference time: 0.10 ms
|2025-01-27 18:19:36| ********************Experiment Success********************
```

