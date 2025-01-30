```python
|2025-01-28 20:06:20| {
     'ablation': 1, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': protocol, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e382e8b2bd0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-28 20:06:20| ********************Experiment Start********************
|2025-01-28 20:06:43| Round=1 BestEpoch= 63 Ac=0.5839 Pr=0.5938 Rc=0.5572 F1=0.5637 Training_time=7.0 s 

|2025-01-28 20:07:05| Round=2 BestEpoch= 57 Ac=0.6095 Pr=0.6483 Rc=0.6103 F1=0.6090 Training_time=6.2 s 

|2025-01-28 20:07:05| ********************Experiment Results:********************
|2025-01-28 20:07:05| AC: 0.5967 ± 0.0128
|2025-01-28 20:07:05| PR: 0.6210 ± 0.0273
|2025-01-28 20:07:05| RC: 0.5838 ± 0.0266
|2025-01-28 20:07:05| F1: 0.5863 ± 0.0226
|2025-01-28 20:07:05| train_time: 6.5900 ± 0.3773
|2025-01-28 20:07:05| Flops: 89292800
|2025-01-28 20:07:05| Params: 51340
|2025-01-28 20:07:05| Inference time: 0.08 ms
|2025-01-28 20:07:06| ********************Experiment Success********************
```

