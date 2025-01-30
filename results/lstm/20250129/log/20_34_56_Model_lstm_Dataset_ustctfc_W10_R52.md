```python
|2025-01-29 20:34:56| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 10, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x9d8e4b66c00>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 20:34:56| ********************Experiment Start********************
|2025-01-29 20:34:57| Ac=0.8827 Pr=0.7259 Rc=0.7584 F1=0.7283 time=21.4 s 
|2025-01-29 20:34:57| Ac=0.8446 Pr=0.6201 Rc=0.5458 F1=0.5704 time=9.5 s 
|2025-01-29 20:34:57| ********************Experiment Results:********************
|2025-01-29 20:34:57| AC: 0.8636 ± 0.0191
|2025-01-29 20:34:57| PR: 0.6730 ± 0.0529
|2025-01-29 20:34:57| RC: 0.6521 ± 0.1063
|2025-01-29 20:34:57| F1: 0.6494 ± 0.0790
|2025-01-29 20:34:57| train_time: 15.4393 ± 5.9119
|2025-01-29 20:34:57| Flops: 45061120
|2025-01-29 20:34:57| Params: 42345
|2025-01-29 20:34:57| Inference time: 0.07 ms
|2025-01-29 20:34:57| ********************Experiment Success********************
```

