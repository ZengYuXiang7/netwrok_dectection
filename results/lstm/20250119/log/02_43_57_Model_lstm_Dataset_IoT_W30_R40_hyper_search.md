```python
|2025-01-19 02:43:57| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7f65415be3c0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 40, 'record': True, 'retrain': True, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 02:43:57| ********************Experiment Start********************
|2025-01-19 02:47:05| Round=1 BestEpoch=207 Acc=0.8909 F1=0.8219 Precision=0.8314 Recall=0.8167 Training_time=134.5 s 

|2025-01-19 02:47:05| ********************Experiment Results:********************
|2025-01-19 02:47:05| Acc: 0.8909 ± 0.0000
|2025-01-19 02:47:05| F1: 0.8219 ± 0.0000
|2025-01-19 02:47:05| P: 0.8314 ± 0.0000
|2025-01-19 02:47:05| Recall: 0.8167 ± 0.0000
|2025-01-19 02:47:05| train_time: 134.4528 ± 0.0000
|2025-01-19 02:47:05| Flops: 82483200
|2025-01-19 02:47:05| Params: 45221
|2025-01-19 02:47:05| Inference time: 0.08 ms
|2025-01-19 02:47:05| ********************Experiment Success********************
```

