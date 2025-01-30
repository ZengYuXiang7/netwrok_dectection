```python
|2025-01-30 16:26:33| {
     'ablation': 1, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': ustctfc, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x75fda21b8920>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 60, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-30 16:26:33| ********************Experiment Start********************
|2025-01-30 16:28:23| Round=1 BestEpoch=192 Ac=0.8835 Pr=0.5557 Rc=0.4572 F1=0.4798 Training_time=19.8 s 

|2025-01-30 16:29:01| Round=2 BestEpoch=159 Ac=0.8608 Pr=0.4828 Rc=0.4650 F1=0.4714 Training_time=16.4 s 

|2025-01-30 16:29:01| ********************Experiment Results:********************
|2025-01-30 16:29:01| AC: 0.8722 ± 0.0113
|2025-01-30 16:29:01| PR: 0.5193 ± 0.0365
|2025-01-30 16:29:01| RC: 0.4611 ± 0.0039
|2025-01-30 16:29:01| F1: 0.4756 ± 0.0042
|2025-01-30 16:29:01| train_time: 18.0682 ± 1.7165
|2025-01-30 16:29:01| Flops: 90275840
|2025-01-30 16:29:01| Params: 59026
|2025-01-30 16:29:01| Inference time: 0.07 ms
|2025-01-30 16:29:02| ********************Experiment Success********************
```

