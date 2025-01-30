```python
|2025-01-29 20:15:52| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x5a178aa3470>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 20:15:52| ********************Experiment Start********************
|2025-01-29 20:16:08| Round=1 BestEpoch= 52 Ac=0.8271 Pr=0.7107 Rc=0.5535 F1=0.5958 Training_time=5.2 s 

|2025-01-29 20:16:18| Round=2 BestEpoch= 27 Ac=0.7444 Pr=0.5686 Rc=0.4842 F1=0.4905 Training_time=2.6 s 

|2025-01-29 20:16:18| ********************Experiment Results:********************
|2025-01-29 20:16:18| AC: 0.7857 ± 0.0414
|2025-01-29 20:16:18| PR: 0.6397 ± 0.0711
|2025-01-29 20:16:18| RC: 0.5189 ± 0.0346
|2025-01-29 20:16:18| F1: 0.5431 ± 0.0527
|2025-01-29 20:16:18| train_time: 3.9127 ± 1.2743
|2025-01-29 20:16:18| Flops: 720896
|2025-01-29 20:16:18| Params: 5511
|2025-01-29 20:16:18| Inference time: 0.06 ms
|2025-01-29 20:16:19| ********************Experiment Success********************
```

