```python
|2025-01-09 18:35:15| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x705491b9c9e0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': cnn, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 100,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 18:35:15| ********************Experiment Start********************
|2025-01-09 18:40:32| Round=1 BestEpoch=280 Acc=0.8741 F1=0.8025 Precision=0.8283 Recall=0.7931 Training_time=225.2 s 

|2025-01-09 18:40:32| ********************Experiment Results:********************
|2025-01-09 18:40:32| Acc: 0.8741 ± 0.0000
|2025-01-09 18:40:32| F1: 0.8025 ± 0.0000
|2025-01-09 18:40:32| P: 0.8283 ± 0.0000
|2025-01-09 18:40:32| Recall: 0.7931 ± 0.0000
|2025-01-09 18:40:32| train_time: 225.2494 ± 0.0000
|2025-01-09 18:40:33| Flops: 120089600
|2025-01-09 18:40:33| Params: 33021
|2025-01-09 18:40:33| Inference time: 0.09 ms
|2025-01-09 18:40:33| ********************Experiment Success********************
```

