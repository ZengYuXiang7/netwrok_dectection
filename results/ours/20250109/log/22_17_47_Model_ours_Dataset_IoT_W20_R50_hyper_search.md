```python
|2025-01-09 22:17:47| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x71fb8ee444d0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 22:17:47| ********************Experiment Start********************
|2025-01-09 22:27:15| Round=1 BestEpoch=248 Acc=0.8939 F1=0.8418 Precision=0.8513 Recall=0.8365 Training_time=435.7 s 

|2025-01-09 22:27:15| ********************Experiment Results:********************
|2025-01-09 22:27:15| Acc: 0.8939 ± 0.0000
|2025-01-09 22:27:15| F1: 0.8418 ± 0.0000
|2025-01-09 22:27:15| P: 0.8513 ± 0.0000
|2025-01-09 22:27:15| Recall: 0.8365 ± 0.0000
|2025-01-09 22:27:15| train_time: 435.6941 ± 0.0000
|2025-01-09 22:27:16| Flops: 21833600
|2025-01-09 22:27:16| Params: 67071
|2025-01-09 22:27:16| Inference time: 0.39 ms
|2025-01-09 22:27:16| ********************Experiment Success********************
```

