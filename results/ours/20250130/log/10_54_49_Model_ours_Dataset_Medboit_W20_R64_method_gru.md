```python
|2025-01-30 10:54:49| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': Medboit, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xfdfaf6e8ad0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 60, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-30 10:54:49| ********************Experiment Start********************
|2025-01-30 11:09:43| Round=1 BestEpoch= 99 Ac=0.9810 Pr=0.7812 Rc=0.7127 F1=0.7335 Training_time=48.5 s 

|2025-01-30 11:12:25| Round=2 BestEpoch=173 Ac=0.9762 Pr=0.7734 Rc=0.7342 F1=0.7516 Training_time=84.4 s 

|2025-01-30 11:14:52| Round=3 BestEpoch=148 Ac=0.9679 Pr=0.7910 Rc=0.6823 F1=0.6940 Training_time=73.6 s 

|2025-01-30 11:15:57| Round=4 BestEpoch= 33 Ac=0.9227 Pr=0.5923 Rc=0.6235 F1=0.5994 Training_time=16.2 s 

|2025-01-30 11:17:08| Round=5 BestEpoch= 41 Ac=0.9750 Pr=0.7391 Rc=0.7210 F1=0.7249 Training_time=20.2 s 

|2025-01-30 11:17:08| ********************Experiment Results:********************
|2025-01-30 11:17:08| AC: 0.9646 ± 0.0213
|2025-01-30 11:17:08| PR: 0.7354 ± 0.0737
|2025-01-30 11:17:08| RC: 0.6947 ± 0.0395
|2025-01-30 11:17:08| F1: 0.7007 ± 0.0540
|2025-01-30 11:17:08| train_time: 48.5820 ± 27.4348
|2025-01-30 11:17:09| Flops: 743424000
|2025-01-30 11:17:09| Params: 647814
|2025-01-30 11:17:09| Inference time: 0.89 ms
|2025-01-30 11:17:10| ********************Experiment Success********************
```

