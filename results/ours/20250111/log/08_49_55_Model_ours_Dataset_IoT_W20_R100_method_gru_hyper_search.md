```python
|2025-01-11 08:49:55| {
     'Ablation': 0, 'bidirectional': False, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b4d89fc59d0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 100, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': gru, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 08:49:55| ********************Experiment Start********************
|2025-01-11 08:57:22| Round=1 BestEpoch=166 Acc=0.9196 F1=0.8811 Precision=0.8822 Recall=0.8807 Training_time=328.1 s 

|2025-01-11 08:57:22| ********************Experiment Results:********************
|2025-01-11 08:57:22| Acc: 0.9196 ± 0.0000
|2025-01-11 08:57:22| F1: 0.8811 ± 0.0000
|2025-01-11 08:57:22| P: 0.8822 ± 0.0000
|2025-01-11 08:57:22| Recall: 0.8807 ± 0.0000
|2025-01-11 08:57:22| train_time: 328.1421 ± 0.0000
|2025-01-11 08:57:23| Flops: 398268800
|2025-01-11 08:57:23| Params: 383621
|2025-01-11 08:57:23| Inference time: 0.33 ms
|2025-01-11 08:57:24| ********************Experiment Success********************
```

