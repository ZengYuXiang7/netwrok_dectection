```python
|2025-01-29 12:14:46| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xa31772a1b20>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 12:14:46| ********************Experiment Start********************
|2025-01-29 12:16:34| Round=1 BestEpoch=122 Ac=0.5871 Pr=0.5349 Rc=0.4516 F1=0.4395 Training_time=67.3 s 

|2025-01-29 12:18:07| Round=2 BestEpoch= 99 Ac=0.5930 Pr=0.4230 Rc=0.4301 F1=0.4050 Training_time=55.7 s 

|2025-01-29 12:18:07| ********************Experiment Results:********************
|2025-01-29 12:18:07| AC: 0.5901 ± 0.0030
|2025-01-29 12:18:07| PR: 0.4790 ± 0.0560
|2025-01-29 12:18:07| RC: 0.4408 ± 0.0108
|2025-01-29 12:18:07| F1: 0.4223 ± 0.0172
|2025-01-29 12:18:07| train_time: 61.5115 ± 5.7875
|2025-01-29 12:18:07| Flops: 22503936
|2025-01-29 12:18:07| Params: 9640
|2025-01-29 12:18:07| Inference time: 0.09 ms
|2025-01-29 12:18:08| ********************Experiment Success********************
```

