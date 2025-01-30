```python
|2025-01-18 12:00:35| {
     'Ablation': 0, 'bs': 150, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x9ab4f903050>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': dapp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 12:00:35| ********************Experiment Start********************
|2025-01-18 12:09:51| Round=1 BestEpoch=255 Acc=0.6189 F1=0.5036 Precision=0.6020 Recall=0.4899 Training_time=406.7 s 

|2025-01-18 12:09:52| ********************Experiment Results:********************
|2025-01-18 12:09:52| Acc: 0.6189 ± 0.0000
|2025-01-18 12:09:52| F1: 0.5036 ± 0.0000
|2025-01-18 12:09:52| P: 0.6020 ± 0.0000
|2025-01-18 12:09:52| Recall: 0.4899 ± 0.0000
|2025-01-18 12:09:52| train_time: 406.6650 ± 0.0000
|2025-01-18 12:10:07| Flops: 114940800
|2025-01-18 12:10:07| Params: 29525
|2025-01-18 12:10:07| Inference time: 0.71 ms
|2025-01-18 12:10:08| ********************Experiment Success********************
```

