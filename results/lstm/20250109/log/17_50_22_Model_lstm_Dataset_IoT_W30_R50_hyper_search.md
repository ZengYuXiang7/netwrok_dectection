```python
|2025-01-09 17:50:22| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b1c7a13aba0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': lstm, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 17:50:22| ********************Experiment Start********************
|2025-01-09 17:55:13| Round=1 BestEpoch=258 Acc=0.8611 F1=0.7891 Precision=0.7942 Recall=0.7863 Training_time=205.9 s 

|2025-01-09 17:55:13| ********************Experiment Results:********************
|2025-01-09 17:55:13| Acc: 0.8611 ± 0.0000
|2025-01-09 17:55:13| F1: 0.7891 ± 0.0000
|2025-01-09 17:55:13| P: 0.7942 ± 0.0000
|2025-01-09 17:55:13| Recall: 0.7863 ± 0.0000
|2025-01-09 17:55:13| train_time: 205.9043 ± 0.0000
|2025-01-09 17:55:14| Flops: 126144000
|2025-01-09 17:55:14| Params: 62521
|2025-01-09 17:55:14| Inference time: 0.07 ms
|2025-01-09 17:55:14| ********************Experiment Success********************
```

