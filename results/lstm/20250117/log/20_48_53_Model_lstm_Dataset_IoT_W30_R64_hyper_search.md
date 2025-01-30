```python
|2025-01-17 20:48:53| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7346e7450050>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-17 20:48:53| ********************Experiment Start********************
|2025-01-17 20:51:30| Round=1 BestEpoch=179 Acc=0.8502 F1=0.7743 Precision=0.7816 Recall=0.7710 Training_time=111.6 s 

|2025-01-17 20:51:30| ********************Experiment Results:********************
|2025-01-17 20:51:30| Acc: 0.8502 ± 0.0000
|2025-01-17 20:51:30| F1: 0.7743 ± 0.0000
|2025-01-17 20:51:30| P: 0.7816 ± 0.0000
|2025-01-17 20:51:30| Recall: 0.7710 ± 0.0000
|2025-01-17 20:51:30| train_time: 111.6228 ± 0.0000
|2025-01-17 20:51:31| Flops: 202752000
|2025-01-17 20:51:31| Params: 90773
|2025-01-17 20:51:31| Inference time: 0.07 ms
|2025-01-17 20:51:31| ********************Experiment Success********************
```

