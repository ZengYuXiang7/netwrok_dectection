```python
|2025-01-19 02:52:19| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x128f34e73dd0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 02:52:19| ********************Experiment Start********************
|2025-01-19 02:52:20| Acc=0.8885 F1=0.8229 Precision=0.8268 Recall=0.8209 time=116.4 s 
|2025-01-19 02:52:20| ********************Experiment Results:********************
|2025-01-19 02:52:20| Acc: 0.8885 ± 0.0000
|2025-01-19 02:52:20| F1: 0.8229 ± 0.0000
|2025-01-19 02:52:20| P: 0.8268 ± 0.0000
|2025-01-19 02:52:20| Recall: 0.8209 ± 0.0000
|2025-01-19 02:52:20| train_time: 116.4205 ± 0.0000
|2025-01-19 02:52:20| Flops: 179020800
|2025-01-19 02:52:20| Params: 82221
|2025-01-19 02:52:20| Inference time: 0.08 ms
|2025-01-19 02:52:20| ********************Experiment Success********************
```

