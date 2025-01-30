```python
|2025-01-29 20:41:15| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x15410997b140>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 20:41:15| ********************Experiment Start********************
|2025-01-29 20:42:48| Round=1 BestEpoch= 40 Ac=0.9126 Pr=0.5524 Rc=0.5478 F1=0.5456 Training_time=7.5 s 

|2025-01-29 20:43:08| Round=2 BestEpoch= 23 Ac=0.8803 Pr=0.5591 Rc=0.5604 F1=0.5577 Training_time=4.2 s 

|2025-01-29 20:43:08| ********************Experiment Results:********************
|2025-01-29 20:43:08| AC: 0.8964 ± 0.0162
|2025-01-29 20:43:08| PR: 0.5557 ± 0.0033
|2025-01-29 20:43:08| RC: 0.5541 ± 0.0063
|2025-01-29 20:43:08| F1: 0.5516 ± 0.0061
|2025-01-29 20:43:08| train_time: 5.8482 ± 1.6541
|2025-01-29 20:43:09| Flops: 493888512
|2025-01-29 20:43:09| Params: 429642
|2025-01-29 20:43:09| Inference time: 0.89 ms
|2025-01-29 20:43:09| ********************Experiment Success********************
```

