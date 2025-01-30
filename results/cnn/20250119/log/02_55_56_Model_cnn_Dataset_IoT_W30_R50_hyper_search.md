```python
|2025-01-19 02:55:56| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x72b0009dcc80>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': True, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 02:55:56| ********************Experiment Start********************
|2025-01-19 02:58:23| Round=1 BestEpoch=157 Acc=0.8590 F1=0.7800 Precision=0.8122 Recall=0.7856 Training_time=98.9 s 

|2025-01-19 02:58:23| ********************Experiment Results:********************
|2025-01-19 02:58:23| Acc: 0.8590 ± 0.0000
|2025-01-19 02:58:23| F1: 0.7800 ± 0.0000
|2025-01-19 02:58:23| P: 0.8122 ± 0.0000
|2025-01-19 02:58:23| Recall: 0.7856 ± 0.0000
|2025-01-19 02:58:23| train_time: 98.8788 ± 0.0000
|2025-01-19 02:58:23| Flops: 31244800
|2025-01-19 02:58:23| Params: 9021
|2025-01-19 02:58:23| Inference time: 0.09 ms
|2025-01-19 02:58:24| ********************Experiment Success********************
```

