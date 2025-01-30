```python
|2025-01-25 22:14:34| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': protocol, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 10, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x7938c54531a0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-25 22:14:34| ********************Experiment Start********************
|2025-01-25 22:21:27| Round=1 BestEpoch=154 Acc=0.6451 F1=0.5645 Precision=0.5843 Recall=0.5763 Training_time=30.8 s 

|2025-01-25 22:22:09| Round=2 BestEpoch= 80 Acc=0.6283 F1=0.5534 Precision=0.5879 Recall=0.5517 Training_time=16.0 s 

|2025-01-25 22:22:09| ********************Experiment Results:********************
|2025-01-25 22:22:09| Acc: 0.6367 ± 0.0084
|2025-01-25 22:22:09| F1: 0.5590 ± 0.0056
|2025-01-25 22:22:09| P: 0.5861 ± 0.0018
|2025-01-25 22:22:09| Recall: 0.5640 ± 0.0123
|2025-01-25 22:22:09| train_time: 23.3591 ± 7.4089
|2025-01-25 22:22:09| Flops: 371818496
|2025-01-25 22:22:09| Params: 324686
|2025-01-25 22:22:09| Inference time: 0.55 ms
|2025-01-25 22:22:10| ********************Experiment Success********************
```

