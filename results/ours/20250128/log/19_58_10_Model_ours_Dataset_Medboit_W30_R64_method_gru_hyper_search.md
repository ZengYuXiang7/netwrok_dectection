```python
|2025-01-28 19:58:10| {
     'ablation': 1, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': Medboit, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a2d9aa0fc20>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-28 19:58:10| ********************Experiment Start********************
|2025-01-28 19:59:18| Round=1 BestEpoch=203 Ac=0.7130 Pr=0.6655 Rc=0.6431 F1=0.6524 Training_time=33.8 s 

|2025-01-28 20:00:13| Round=2 BestEpoch=155 Ac=0.7120 Pr=0.6622 Rc=0.6462 F1=0.6530 Training_time=26.3 s 

|2025-01-28 20:00:13| ********************Experiment Results:********************
|2025-01-28 20:00:13| AC: 0.7125 ± 0.0005
|2025-01-28 20:00:13| PR: 0.6638 ± 0.0016
|2025-01-28 20:00:13| RC: 0.6447 ± 0.0016
|2025-01-28 20:00:13| F1: 0.6527 ± 0.0003
|2025-01-28 20:00:13| train_time: 30.0621 ± 3.7706
|2025-01-28 20:00:14| Flops: 132956160
|2025-01-28 20:00:14| Params: 52616
|2025-01-28 20:00:14| Inference time: 0.08 ms
|2025-01-28 20:00:14| ********************Experiment Success********************
```

