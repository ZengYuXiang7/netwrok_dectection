```python
|2025-01-29 11:53:33| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x5db59812690>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 11:53:33| ********************Experiment Start********************
|2025-01-29 12:00:53| Round=1 BestEpoch= 82 Ac=0.6060 Pr=0.4789 Rc=0.4919 F1=0.4700 Training_time=184.8 s 

|2025-01-29 12:05:36| Round=2 BestEpoch= 68 Ac=0.6058 Pr=0.4946 Rc=0.4441 F1=0.4422 Training_time=151.1 s 

|2025-01-29 12:05:36| ********************Experiment Results:********************
|2025-01-29 12:05:36| AC: 0.6059 ± 0.0001
|2025-01-29 12:05:36| PR: 0.4868 ± 0.0078
|2025-01-29 12:05:36| RC: 0.4680 ± 0.0239
|2025-01-29 12:05:36| F1: 0.4561 ± 0.0139
|2025-01-29 12:05:36| train_time: 167.9610 ± 16.8808
|2025-01-29 12:05:37| Flops: 493901824
|2025-01-29 12:05:37| Params: 429748
|2025-01-29 12:05:37| Inference time: 0.86 ms
|2025-01-29 12:05:37| ********************Experiment Success********************
```

