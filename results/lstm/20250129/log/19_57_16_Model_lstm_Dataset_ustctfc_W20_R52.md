```python
|2025-01-29 19:57:16| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xa98a299a240>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 19:57:16| ********************Experiment Start********************
|2025-01-29 19:57:30| Round=1 BestEpoch= 38 Ac=0.8600 Pr=0.7455 Rc=0.7085 F1=0.7147 Training_time=4.3 s 

|2025-01-29 19:57:42| Round=2 BestEpoch= 28 Ac=0.8200 Pr=0.5699 Rc=0.5545 F1=0.5558 Training_time=3.1 s 

|2025-01-29 19:57:42| ********************Experiment Results:********************
|2025-01-29 19:57:42| AC: 0.8400 ± 0.0200
|2025-01-29 19:57:42| PR: 0.6577 ± 0.0878
|2025-01-29 19:57:42| RC: 0.6315 ± 0.0770
|2025-01-29 19:57:42| F1: 0.6353 ± 0.0794
|2025-01-29 19:57:42| train_time: 3.6792 ± 0.5827
|2025-01-29 19:57:42| Flops: 90122240
|2025-01-29 19:57:42| Params: 51185
|2025-01-29 19:57:42| Inference time: 0.07 ms
|2025-01-29 19:57:43| ********************Experiment Success********************
```

