```python
|2025-01-28 16:34:38| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': Medboit, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x1536e5ff6cc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-28 16:34:38| ********************Experiment Start********************
|2025-01-28 16:35:56| Round=1 BestEpoch= 58 Ac=0.7448 Pr=0.6989 Rc=0.6761 F1=0.6865 Training_time=34.0 s 

|2025-01-28 16:37:07| Round=2 BestEpoch= 48 Ac=0.6822 Pr=0.6242 Rc=0.6398 F1=0.6306 Training_time=28.9 s 

|2025-01-28 16:37:07| ********************Experiment Results:********************
|2025-01-28 16:37:07| AC: 0.7135 ± 0.0313
|2025-01-28 16:37:07| PR: 0.6616 ± 0.0374
|2025-01-28 16:37:07| RC: 0.6580 ± 0.0182
|2025-01-28 16:37:07| F1: 0.6586 ± 0.0279
|2025-01-28 16:37:07| train_time: 31.4819 ± 2.5607
|2025-01-28 16:37:07| Flops: 1115111424
|2025-01-28 16:37:07| Params: 971592
|2025-01-28 16:37:07| Inference time: 1.20 ms
|2025-01-28 16:37:07| ********************Experiment Success********************
```

