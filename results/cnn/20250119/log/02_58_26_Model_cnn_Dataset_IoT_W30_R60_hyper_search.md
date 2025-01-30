```python
|2025-01-19 02:58:26| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x773ce187c650>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': True, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 02:58:26| ********************Experiment Start********************
|2025-01-19 03:03:20| Round=1 BestEpoch=365 Acc=0.8977 F1=0.8345 Precision=0.8583 Recall=0.8214 Training_time=216.1 s 

|2025-01-19 03:03:20| ********************Experiment Results:********************
|2025-01-19 03:03:20| Acc: 0.8977 ± 0.0000
|2025-01-19 03:03:20| F1: 0.8345 ± 0.0000
|2025-01-19 03:03:20| P: 0.8583 ± 0.0000
|2025-01-19 03:03:20| Recall: 0.8214 ± 0.0000
|2025-01-19 03:03:20| train_time: 216.0773 ± 0.0000
|2025-01-19 03:03:20| Flops: 44405760
|2025-01-19 03:03:20| Params: 12621
|2025-01-19 03:03:20| Inference time: 0.09 ms
|2025-01-19 03:03:21| ********************Experiment Success********************
```

