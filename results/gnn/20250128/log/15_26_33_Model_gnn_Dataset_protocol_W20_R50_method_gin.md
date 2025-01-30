```python
|2025-01-28 15:26:33| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gin, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x128d80aaf080>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 2, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 2, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-28 15:26:33| ********************Experiment Start********************
|2025-01-28 15:26:48| Round=1 BestEpoch= 20 Ac=0.5730 Pr=0.6231 Rc=0.5531 F1=0.5759 Training_time=3.4 s 

|2025-01-28 15:27:03| Round=2 BestEpoch= 21 Ac=0.5693 Pr=0.6355 Rc=0.5545 F1=0.5797 Training_time=3.6 s 

|2025-01-28 15:27:03| ********************Experiment Results:********************
|2025-01-28 15:27:03| AC: 0.5712 ± 0.0018
|2025-01-28 15:27:03| PR: 0.6293 ± 0.0062
|2025-01-28 15:27:03| RC: 0.5538 ± 0.0007
|2025-01-28 15:27:03| F1: 0.5778 ± 0.0019
|2025-01-28 15:27:03| train_time: 3.4869 ± 0.1085
|2025-01-28 15:27:04| Flops: 4288000
|2025-01-28 15:27:04| Params: 14762
|2025-01-28 15:27:04| Inference time: 0.24 ms
|2025-01-28 15:27:04| ********************Experiment Success********************
```

