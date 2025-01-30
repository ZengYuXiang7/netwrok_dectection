```python
|2025-01-30 16:19:21| {
     'ablation': 1, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': Medboit, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7554d427d460>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 60, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-30 16:19:21| ********************Experiment Start********************
|2025-01-30 16:20:15| Round=1 BestEpoch=191 Ac=0.9620 Pr=0.6750 Rc=0.6675 F1=0.6664 Training_time=26.4 s 

|2025-01-30 16:21:23| Round=2 BestEpoch=255 Ac=0.9548 Pr=0.6061 Rc=0.5969 F1=0.6009 Training_time=35.4 s 

|2025-01-30 16:21:23| ********************Experiment Results:********************
|2025-01-30 16:21:23| AC: 0.9584 ± 0.0036
|2025-01-30 16:21:23| PR: 0.6406 ± 0.0345
|2025-01-30 16:21:23| RC: 0.6322 ± 0.0353
|2025-01-30 16:21:23| F1: 0.6337 ± 0.0328
|2025-01-30 16:21:23| train_time: 30.8757 ± 4.4980
|2025-01-30 16:21:23| Flops: 88309760
|2025-01-30 16:21:23| Params: 43654
|2025-01-30 16:21:23| Inference time: 0.07 ms
|2025-01-30 16:21:24| ********************Experiment Success********************
```

