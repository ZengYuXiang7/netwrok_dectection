```python
|2025-01-18 00:02:47| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7aac432f0050>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 00:02:47| ********************Experiment Start********************
|2025-01-18 00:08:26| Round=1 BestEpoch=455 Acc=0.8221 F1=0.7200 Precision=0.7377 Recall=0.7105 Training_time=258.1 s 

|2025-01-18 00:08:26| ********************Experiment Results:********************
|2025-01-18 00:08:26| Acc: 0.8221 ± 0.0000
|2025-01-18 00:08:26| F1: 0.7200 ± 0.0000
|2025-01-18 00:08:26| P: 0.7377 ± 0.0000
|2025-01-18 00:08:26| Recall: 0.7105 ± 0.0000
|2025-01-18 00:08:26| train_time: 258.0973 ± 0.0000
|2025-01-18 00:08:26| Flops: 20387840
|2025-01-18 00:08:26| Params: 6021
|2025-01-18 00:08:26| Inference time: 0.09 ms
|2025-01-18 00:08:26| ********************Experiment Success********************
```

