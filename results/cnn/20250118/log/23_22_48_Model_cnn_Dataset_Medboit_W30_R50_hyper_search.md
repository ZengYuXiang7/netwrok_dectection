```python
|2025-01-18 23:22:48| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7ab1af3991c0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 23:22:48| ********************Experiment Start********************
|2025-01-18 23:23:33| Round=1 BestEpoch= 76 Acc=0.9186 F1=0.6579 Precision=0.7102 Recall=0.6431 Training_time=24.8 s 

|2025-01-18 23:23:33| ********************Experiment Results:********************
|2025-01-18 23:23:33| Acc: 0.9186 ± 0.0000
|2025-01-18 23:23:33| F1: 0.6579 ± 0.0000
|2025-01-18 23:23:33| P: 0.7102 ± 0.0000
|2025-01-18 23:23:33| Recall: 0.6431 ± 0.0000
|2025-01-18 23:23:33| train_time: 24.7504 ± 0.0000
|2025-01-18 23:23:34| Flops: 31161600
|2025-01-18 23:23:34| Params: 8358
|2025-01-18 23:23:34| Inference time: 0.09 ms
|2025-01-18 23:23:34| ********************Experiment Success********************
```

