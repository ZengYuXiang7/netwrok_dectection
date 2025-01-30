```python
|2025-01-29 21:59:16| {
     'ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x10dd1294c620>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-29 21:59:16| ********************Experiment Start********************
|2025-01-29 21:59:16| Ac=0.8964 Pr=0.5603 Rc=0.4783 F1=0.5006 time=2.2 s 
|2025-01-29 21:59:16| Ac=0.8738 Pr=0.5342 Rc=0.5571 F1=0.5441 time=13.9 s 
|2025-01-29 21:59:16| ********************Experiment Results:********************
|2025-01-29 21:59:16| AC: 0.8851 ± 0.0113
|2025-01-29 21:59:16| PR: 0.5472 ± 0.0131
|2025-01-29 21:59:16| RC: 0.5177 ± 0.0394
|2025-01-29 21:59:16| F1: 0.5224 ± 0.0217
|2025-01-29 21:59:16| train_time: 8.0426 ± 5.8080
|2025-01-29 21:59:17| Flops: 493888512
|2025-01-29 21:59:17| Params: 429642
|2025-01-29 21:59:17| Inference time: 1.08 ms
