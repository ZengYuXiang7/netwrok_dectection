```python
|2025-01-28 20:08:22| {
     'ablation': 3, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': protocol, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7aa2f8bb6ea0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-28 20:08:22| ********************Experiment Start********************
|2025-01-28 20:08:50| Round=1 BestEpoch= 68 Ac=0.6022 Pr=0.6656 Rc=0.5999 F1=0.6241 Training_time=8.8 s 

|2025-01-28 20:09:30| Round=2 BestEpoch=132 Ac=0.6423 Pr=0.6591 Rc=0.6138 F1=0.6264 Training_time=16.7 s 

|2025-01-28 20:09:30| ********************Experiment Results:********************
|2025-01-28 20:09:30| AC: 0.6223 ± 0.0201
|2025-01-28 20:09:30| PR: 0.6624 ± 0.0033
|2025-01-28 20:09:30| RC: 0.6068 ± 0.0070
|2025-01-28 20:09:30| F1: 0.6253 ± 0.0011
|2025-01-28 20:09:30| train_time: 12.7361 ± 3.9342
|2025-01-28 20:09:30| Flops: 75825152
|2025-01-28 20:09:30| Params: 91980
|2025-01-28 20:09:30| Inference time: 0.36 ms
|2025-01-28 20:09:31| ********************Experiment Success********************
```

