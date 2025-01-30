```python
|2025-01-28 15:24:13| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x76b310aacc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-28 15:24:13| ********************Experiment Start********************
|2025-01-28 15:24:59| Round=1 BestEpoch=168 Ac=0.6642 Pr=0.6636 Rc=0.6173 F1=0.6308 Training_time=20.7 s 

|2025-01-28 15:25:38| Round=2 BestEpoch=144 Ac=0.6460 Pr=0.7357 Rc=0.7044 F1=0.7116 Training_time=17.5 s 

|2025-01-28 15:25:38| ********************Experiment Results:********************
|2025-01-28 15:25:38| AC: 0.6551 ± 0.0091
|2025-01-28 15:25:38| PR: 0.6996 ± 0.0361
|2025-01-28 15:25:38| RC: 0.6609 ± 0.0435
|2025-01-28 15:25:38| F1: 0.6712 ± 0.0404
|2025-01-28 15:25:38| train_time: 19.0987 ± 1.5902
|2025-01-28 15:25:39| Flops: 20819200
|2025-01-28 15:25:39| Params: 8562
|2025-01-28 15:25:39| Inference time: 0.10 ms
|2025-01-28 15:25:39| ********************Experiment Success********************
```

