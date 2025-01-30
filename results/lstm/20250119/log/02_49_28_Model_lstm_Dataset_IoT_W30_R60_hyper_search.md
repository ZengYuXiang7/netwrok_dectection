```python
|2025-01-19 02:49:28| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d52e942f740>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': True, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 02:49:28| ********************Experiment Start********************
|2025-01-19 02:52:16| Round=1 BestEpoch=174 Acc=0.8939 F1=0.8308 Precision=0.8357 Recall=0.8281 Training_time=116.4 s 

|2025-01-19 02:52:16| ********************Experiment Results:********************
|2025-01-19 02:52:16| Acc: 0.8939 ± 0.0000
|2025-01-19 02:52:16| F1: 0.8308 ± 0.0000
|2025-01-19 02:52:16| P: 0.8357 ± 0.0000
|2025-01-19 02:52:16| Recall: 0.8281 ± 0.0000
|2025-01-19 02:52:16| train_time: 116.4205 ± 0.0000
|2025-01-19 02:52:16| Flops: 179020800
|2025-01-19 02:52:16| Params: 82221
|2025-01-19 02:52:16| Inference time: 0.07 ms
|2025-01-19 02:52:17| ********************Experiment Success********************
```

