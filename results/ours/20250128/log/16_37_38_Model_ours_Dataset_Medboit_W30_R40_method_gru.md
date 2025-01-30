```python
|2025-01-28 16:37:38| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': Medboit, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x701bac26540>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 40,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-28 16:37:38| ********************Experiment Start********************
|2025-01-28 16:39:17| Round=1 BestEpoch= 90 Ac=0.7547 Pr=0.7052 Rc=0.6836 F1=0.6929 Training_time=52.8 s 

|2025-01-28 16:40:36| Round=2 BestEpoch= 61 Ac=0.7607 Pr=0.7122 Rc=0.7043 F1=0.7078 Training_time=35.6 s 

|2025-01-28 16:40:36| ********************Experiment Results:********************
|2025-01-28 16:40:36| AC: 0.7577 ± 0.0030
|2025-01-28 16:40:36| PR: 0.7087 ± 0.0035
|2025-01-28 16:40:36| RC: 0.6940 ± 0.0103
|2025-01-28 16:40:36| F1: 0.7003 ± 0.0075
|2025-01-28 16:40:36| train_time: 44.2013 ± 8.5922
|2025-01-28 16:40:36| Flops: 442583040
|2025-01-28 16:40:36| Params: 382608
|2025-01-28 16:40:36| Inference time: 1.21 ms
|2025-01-28 16:40:37| ********************Experiment Success********************
```

