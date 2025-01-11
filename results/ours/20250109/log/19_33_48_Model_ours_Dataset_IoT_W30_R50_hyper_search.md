```python
|2025-01-09 19:33:48| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e4885b70410>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 19:33:48| ********************Experiment Start********************
|2025-01-09 19:40:45| Round=1 BestEpoch=300 Acc=0.8558 F1=0.7891 Precision=0.8068 Recall=0.7824 Training_time=311.4 s 

|2025-01-09 19:40:45| ********************Experiment Results:********************
|2025-01-09 19:40:45| Acc: 0.8558 ± 0.0000
|2025-01-09 19:40:45| F1: 0.7891 ± 0.0000
|2025-01-09 19:40:45| P: 0.8068 ± 0.0000
|2025-01-09 19:40:45| Recall: 0.7824 ± 0.0000
|2025-01-09 19:40:45| train_time: 311.3571 ± 0.0000
|2025-01-09 19:40:46| Flops: 133321600
|2025-01-09 19:40:46| Params: 118671
|2025-01-09 19:40:46| Inference time: 0.28 ms
|2025-01-09 19:40:46| ********************Experiment Success********************
```

