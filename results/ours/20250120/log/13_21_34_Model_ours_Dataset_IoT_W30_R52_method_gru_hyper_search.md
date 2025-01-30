```python
|2025-01-20 13:21:34| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c04c7fa2600>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 1, 'num_classes': 21, 'num_layers': 1, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 13:21:34| ********************Experiment Start********************
|2025-01-20 13:24:50| Round=1 BestEpoch= 51 Acc=0.9126 F1=0.8550 Precision=0.8714 Recall=0.8525 Training_time=115.4 s 

|2025-01-20 13:33:04| Round=2 BestEpoch=173 Acc=0.9216 F1=0.8699 Precision=0.8756 Recall=0.8664 Training_time=393.4 s 

|2025-01-20 13:33:04| ********************Experiment Results:********************
|2025-01-20 13:33:04| Acc: 0.9171 ± 0.0045
|2025-01-20 13:33:04| F1: 0.8624 ± 0.0074
|2025-01-20 13:33:04| P: 0.8735 ± 0.0021
|2025-01-20 13:33:04| Recall: 0.8595 ± 0.0070
|2025-01-20 13:33:04| train_time: 254.3977 ± 138.9825
|2025-01-20 13:33:04| Flops: 375737856
|2025-01-20 13:33:04| Params: 363345
|2025-01-20 13:33:04| Inference time: 0.73 ms
|2025-01-20 13:33:05| ********************Experiment Success********************
```

