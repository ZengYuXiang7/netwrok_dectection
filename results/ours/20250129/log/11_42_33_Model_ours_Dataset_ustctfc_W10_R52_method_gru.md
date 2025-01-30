```python
|2025-01-29 11:42:33| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 10, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xf3111caeea0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 11:42:33| ********************Experiment Start********************
|2025-01-29 11:47:42| Round=1 BestEpoch= 52 Ac=0.6027 Pr=0.6669 Rc=0.6230 F1=0.6270 Training_time=87.4 s 

|2025-01-29 11:50:39| Round=2 BestEpoch= 45 Ac=0.5972 Pr=0.5857 Rc=0.5612 F1=0.5566 Training_time=75.5 s 

|2025-01-29 11:50:39| ********************Experiment Results:********************
|2025-01-29 11:50:39| AC: 0.6000 ± 0.0027
|2025-01-29 11:50:39| PR: 0.6263 ± 0.0406
|2025-01-29 11:50:39| RC: 0.5921 ± 0.0309
|2025-01-29 11:50:39| F1: 0.5918 ± 0.0352
|2025-01-29 11:50:39| train_time: 81.4372 ± 5.9550
|2025-01-29 11:50:39| Flops: 247030784
|2025-01-29 11:50:39| Params: 215456
|2025-01-29 11:50:39| Inference time: 0.54 ms
|2025-01-29 11:50:40| ********************Experiment Success********************
```

