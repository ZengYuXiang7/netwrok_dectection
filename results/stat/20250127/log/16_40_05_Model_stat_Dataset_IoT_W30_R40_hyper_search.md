```python
|2025-01-27 16:40:05| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x71faa80b2ff0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': stat, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': True, 'rounds': 2,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-27 16:40:05| ********************Experiment Start********************
|2025-01-27 16:41:41| Round=1 BestEpoch= 59 Acc=0.8174 F1=0.7871 Precision=0.8276 Recall=0.7712 Training_time=52.3 s 

|2025-01-27 16:45:02| Round=2 BestEpoch=154 Acc=0.8357 F1=0.7975 Precision=0.8190 Recall=0.7882 Training_time=138.7 s 

|2025-01-27 16:45:02| ********************Experiment Results:********************
|2025-01-27 16:45:02| Acc: 0.8266 ± 0.0092
|2025-01-27 16:45:02| F1: 0.7923 ± 0.0052
|2025-01-27 16:45:02| P: 0.8233 ± 0.0043
|2025-01-27 16:45:02| Recall: 0.7797 ± 0.0085
|2025-01-27 16:45:02| train_time: 95.5081 ± 43.1621
|2025-01-27 16:45:02| Flops: 169216
|2025-01-27 16:45:02| Params: 2583
|2025-01-27 16:45:02| Inference time: 0.05 ms
|2025-01-27 16:45:03| ********************Experiment Success********************
```

