```python
|2025-01-28 19:16:03| {
     'ablation': 1, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x773bc075f110>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-28 19:16:03| ********************Experiment Start********************
|2025-01-28 19:19:09| Round=1 BestEpoch=179 Ac=0.8601 Pr=0.7954 Rc=0.7809 F1=0.7860 Training_time=118.0 s 

|2025-01-28 19:22:08| Round=2 BestEpoch=170 Ac=0.8696 Pr=0.8117 Rc=0.8038 F1=0.8054 Training_time=111.7 s 

|2025-01-28 19:22:08| ********************Experiment Results:********************
|2025-01-28 19:22:08| AC: 0.8649 ± 0.0047
|2025-01-28 19:22:08| PR: 0.8036 ± 0.0081
|2025-01-28 19:22:08| RC: 0.7924 ± 0.0115
|2025-01-28 19:22:08| F1: 0.7957 ± 0.0097
|2025-01-28 19:22:08| train_time: 114.8411 ± 3.1372
|2025-01-28 19:22:08| Flops: 136151040
|2025-01-28 19:22:08| Params: 77589
|2025-01-28 19:22:08| Inference time: 0.08 ms
|2025-01-28 19:22:08| ********************Experiment Success********************
```

