```python
|2025-01-30 16:21:26| {
     'ablation': 2, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': Medboit, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7cfb876de000>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 60, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-30 16:21:26| ********************Experiment Start********************
|2025-01-30 16:21:56| Round=1 BestEpoch= 46 Ac=0.9679 Pr=0.7142 Rc=0.7258 F1=0.7174 Training_time=8.5 s 

|2025-01-30 16:22:25| Round=2 BestEpoch= 51 Ac=0.9727 Pr=0.7413 Rc=0.7004 F1=0.7180 Training_time=9.3 s 

|2025-01-30 16:22:25| ********************Experiment Results:********************
|2025-01-30 16:22:25| AC: 0.9703 ± 0.0024
|2025-01-30 16:22:25| PR: 0.7278 ± 0.0135
|2025-01-30 16:22:25| RC: 0.7131 ± 0.0127
|2025-01-30 16:22:25| F1: 0.7177 ± 0.0003
|2025-01-30 16:22:25| train_time: 8.9122 ± 0.3645
|2025-01-30 16:22:25| Flops: 377077760
|2025-01-30 16:22:25| Params: 223878
|2025-01-30 16:22:25| Inference time: 0.20 ms
|2025-01-30 16:22:26| ********************Experiment Success********************
```

