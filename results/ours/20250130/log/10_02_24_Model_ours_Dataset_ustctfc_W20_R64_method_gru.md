```python
|2025-01-30 10:02:24| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x89b55de3710>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 60, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-30 10:02:24| ********************Experiment Start********************
|2025-01-30 10:06:51| Round=1 BestEpoch= 93 Ac=0.9866 Pr=0.5367 Rc=0.5262 F1=0.5299 Training_time=97.1 s 

|2025-01-30 10:08:39| Round=2 BestEpoch= 32 Ac=0.9873 Pr=0.5733 Rc=0.5500 F1=0.5585 Training_time=33.4 s 

|2025-01-30 10:13:39| Round=3 BestEpoch=192 Ac=0.9825 Pr=0.5065 Rc=0.4836 F1=0.4900 Training_time=201.9 s 

|2025-01-30 10:18:18| Round=4 BestEpoch=176 Ac=0.9856 Pr=0.5552 Rc=0.5744 F1=0.5633 Training_time=184.4 s 

|2025-01-30 10:20:37| Round=5 BestEpoch= 58 Ac=0.9877 Pr=0.5663 Rc=0.5356 F1=0.5236 Training_time=60.4 s 

|2025-01-30 10:20:37| ********************Experiment Results:********************
|2025-01-30 10:20:37| AC: 0.9860 ± 0.0019
|2025-01-30 10:20:37| PR: 0.5476 ± 0.0240
|2025-01-30 10:20:37| RC: 0.5340 ± 0.0300
|2025-01-30 10:20:37| F1: 0.5331 ± 0.0265
|2025-01-30 10:20:37| train_time: 115.4611 ± 66.8278
|2025-01-30 10:20:37| Flops: 743530496
|2025-01-30 10:20:37| Params: 648659
|2025-01-30 10:20:37| Inference time: 0.88 ms
|2025-01-30 10:20:38| ********************Experiment Success********************
```

