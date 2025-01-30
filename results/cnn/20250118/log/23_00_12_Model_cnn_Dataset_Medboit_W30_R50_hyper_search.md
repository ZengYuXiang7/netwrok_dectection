```python
|2025-01-18 23:00:12| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x72ea11fc2b40>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 23:00:12| ********************Experiment Start********************
|2025-01-18 23:00:57| Round=1 BestEpoch= 76 Acc=0.9186 F1=0.6579 Precision=0.7102 Recall=0.6431 Training_time=24.1 s 

|2025-01-18 23:00:57| ********************Experiment Results:********************
|2025-01-18 23:00:57| Acc: 0.9186 ± 0.0000
|2025-01-18 23:00:57| F1: 0.6579 ± 0.0000
|2025-01-18 23:00:57| P: 0.7102 ± 0.0000
|2025-01-18 23:00:57| Recall: 0.6431 ± 0.0000
|2025-01-18 23:00:57| train_time: 24.1413 ± 0.0000
|2025-01-18 23:00:58| Flops: 31161600
|2025-01-18 23:00:58| Params: 8358
|2025-01-18 23:00:58| Inference time: 0.09 ms
|2025-01-18 23:00:58| ********************Experiment Success********************
```

