```python
|2025-01-11 08:15:14| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x717faa64ecc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 64, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': gru, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 08:15:14| ********************Experiment Start********************
|2025-01-11 08:21:51| Round=1 BestEpoch=128 Acc=0.9163 F1=0.8720 Precision=0.8721 Recall=0.8722 Training_time=283.3 s 

|2025-01-11 08:21:51| ********************Experiment Results:********************
|2025-01-11 08:21:51| Acc: 0.9163 ± 0.0000
|2025-01-11 08:21:51| F1: 0.8720 ± 0.0000
|2025-01-11 08:21:51| P: 0.8721 ± 0.0000
|2025-01-11 08:21:51| Recall: 0.8722 ± 0.0000
|2025-01-11 08:21:51| train_time: 283.2572 ± 0.0000
|2025-01-11 08:21:52| Flops: 379360896
|2025-01-11 08:21:52| Params: 241869
|2025-01-11 08:21:52| Inference time: 0.36 ms
|2025-01-11 08:21:53| ********************Experiment Success********************
```

