```python
|2025-01-28 20:07:08| {
     'ablation': 2, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': protocol, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c9a8a787320>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-28 20:07:08| ********************Experiment Start********************
|2025-01-28 20:07:44| Round=1 BestEpoch= 92 Ac=0.6788 Pr=0.6389 Rc=0.6348 F1=0.6318 Training_time=13.3 s 

|2025-01-28 20:08:19| Round=2 BestEpoch= 96 Ac=0.7117 Pr=0.7244 Rc=0.7396 F1=0.7294 Training_time=13.6 s 

|2025-01-28 20:08:19| ********************Experiment Results:********************
|2025-01-28 20:08:19| AC: 0.6953 ± 0.0164
|2025-01-28 20:08:19| PR: 0.6816 ± 0.0428
|2025-01-28 20:08:19| RC: 0.6872 ± 0.0524
|2025-01-28 20:08:19| F1: 0.6806 ± 0.0488
|2025-01-28 20:08:19| train_time: 13.4728 ± 0.1278
|2025-01-28 20:08:19| Flops: 743473152
|2025-01-28 20:08:19| Params: 365516
|2025-01-28 20:08:19| Inference time: 0.34 ms
|2025-01-28 20:08:20| ********************Experiment Success********************
```

