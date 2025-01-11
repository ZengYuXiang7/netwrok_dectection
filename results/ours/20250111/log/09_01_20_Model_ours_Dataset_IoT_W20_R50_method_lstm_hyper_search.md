```python
|2025-01-11 09:01:20| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d1221b80b90>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 50, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': lstm, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 09:01:20| ********************Experiment Start********************
|2025-01-11 09:07:55| Round=1 BestEpoch=122 Acc=0.9160 F1=0.8752 Precision=0.8772 Recall=0.8743 Training_time=279.9 s 

|2025-01-11 09:07:55| ********************Experiment Results:********************
|2025-01-11 09:07:55| Acc: 0.9160 ± 0.0000
|2025-01-11 09:07:55| F1: 0.8752 ± 0.0000
|2025-01-11 09:07:55| P: 0.8772 ± 0.0000
|2025-01-11 09:07:55| Recall: 0.8743 ± 0.0000
|2025-01-11 09:07:55| train_time: 279.8936 ± 0.0000
|2025-01-11 09:07:56| Flops: 298892800
|2025-01-11 09:07:56| Params: 174225
|2025-01-11 09:07:56| Inference time: 0.37 ms
|2025-01-11 09:07:56| ********************Experiment Success********************
```

