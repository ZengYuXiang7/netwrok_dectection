```python
|2025-01-18 00:08:29| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7329ef46c5c0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 00:08:29| ********************Experiment Start********************
|2025-01-18 00:10:31| Round=1 BestEpoch=142 Acc=0.8020 F1=0.7087 Precision=0.7473 Recall=0.7050 Training_time=81.6 s 

|2025-01-18 00:10:31| ********************Experiment Results:********************
|2025-01-18 00:10:31| Acc: 0.8020 ± 0.0000
|2025-01-18 00:10:31| F1: 0.7087 ± 0.0000
|2025-01-18 00:10:31| P: 0.7473 ± 0.0000
|2025-01-18 00:10:31| Recall: 0.7050 ± 0.0000
|2025-01-18 00:10:31| train_time: 81.6244 ± 0.0000
|2025-01-18 00:10:31| Flops: 31244800
|2025-01-18 00:10:31| Params: 9021
|2025-01-18 00:10:31| Inference time: 0.09 ms
|2025-01-18 00:10:32| ********************Experiment Success********************
```

