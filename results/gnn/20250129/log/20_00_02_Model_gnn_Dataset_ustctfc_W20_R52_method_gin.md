```python
|2025-01-29 20:00:02| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x6e2c0f0a540>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 2, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 52, 'record': True,
     'retrain': False, 'rounds': 2, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 20:00:02| ********************Experiment Start********************
|2025-01-29 20:00:34| Round=1 BestEpoch= 87 Ac=0.8250 Pr=0.6285 Rc=0.5637 F1=0.5800 Training_time=13.2 s 

|2025-01-29 20:01:00| Round=2 BestEpoch= 63 Ac=0.8350 Pr=0.6681 Rc=0.6452 F1=0.6318 Training_time=9.8 s 

|2025-01-29 20:01:00| ********************Experiment Results:********************
|2025-01-29 20:01:00| AC: 0.8300 ± 0.0050
|2025-01-29 20:01:00| PR: 0.6483 ± 0.0198
|2025-01-29 20:01:00| RC: 0.6044 ± 0.0408
|2025-01-29 20:01:00| F1: 0.6059 ± 0.0259
|2025-01-29 20:01:00| train_time: 11.5022 ± 1.7117
|2025-01-29 20:01:00| Flops: 4925440
|2025-01-29 20:01:00| Params: 20661
|2025-01-29 20:01:00| Inference time: 0.23 ms
|2025-01-29 20:01:01| ********************Experiment Success********************
```

