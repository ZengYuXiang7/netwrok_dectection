```python
|2025-01-28 20:00:17| {
     'ablation': 2, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': Medboit, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b03ae013b60>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-28 20:00:17| ********************Experiment Start********************
|2025-01-28 20:00:51| Round=1 BestEpoch= 36 Ac=0.7656 Pr=0.7085 Rc=0.6984 F1=0.7020 Training_time=10.2 s 

|2025-01-28 20:01:35| Round=2 BestEpoch= 62 Ac=0.7637 Pr=0.7046 Rc=0.7071 F1=0.7054 Training_time=17.6 s 

|2025-01-28 20:01:35| ********************Experiment Results:********************
|2025-01-28 20:01:35| AC: 0.7646 ± 0.0010
|2025-01-28 20:01:35| PR: 0.7066 ± 0.0019
|2025-01-28 20:01:35| RC: 0.7027 ± 0.0043
|2025-01-28 20:01:35| F1: 0.7037 ± 0.0017
|2025-01-28 20:01:35| train_time: 13.8919 ± 3.7084
|2025-01-28 20:01:35| Flops: 1115111424
|2025-01-28 20:01:35| Params: 406216
|2025-01-28 20:01:35| Inference time: 0.34 ms
|2025-01-28 20:01:36| ********************Experiment Success********************
```

