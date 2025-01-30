```python
|2025-01-29 21:29:02| {
     'ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x694c760a3c0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 52, 'record': True, 'retrain': False, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-29 21:29:02| ********************Experiment Start********************
|2025-01-29 21:29:11| Round=1 BestEpoch= 19 Ac=0.8608 Pr=0.4990 Rc=0.4468 F1=0.4641 Training_time=1.9 s 

|2025-01-29 21:29:21| Round=2 BestEpoch= 29 Ac=0.8252 Pr=0.5354 Rc=0.4472 F1=0.4723 Training_time=2.7 s 

|2025-01-29 21:29:21| ********************Experiment Results:********************
|2025-01-29 21:29:21| AC: 0.8430 ± 0.0178
|2025-01-29 21:29:21| PR: 0.5172 ± 0.0182
|2025-01-29 21:29:21| RC: 0.4470 ± 0.0002
|2025-01-29 21:29:21| F1: 0.4682 ± 0.0041
|2025-01-29 21:29:21| train_time: 2.3009 ± 0.4274
|2025-01-29 21:29:22| Flops: 661504
|2025-01-29 21:29:22| Params: 5046
|2025-01-29 21:29:22| Inference time: 0.06 ms
|2025-01-29 21:29:22| ********************Experiment Success********************
```

