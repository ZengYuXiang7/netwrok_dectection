```python
|2025-01-09 23:34:54| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x72ab1734e8a0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 104,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': self, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:34:54| ********************Experiment Start********************
|2025-01-09 23:34:56| Acc=0.4952 F1=0.4245 Precision=0.4478 Recall=0.4735 time=130.9 s 
|2025-01-09 23:34:56| ********************Experiment Results:********************
|2025-01-09 23:34:56| Acc: 0.4952 ± 0.0000
|2025-01-09 23:34:56| F1: 0.4245 ± 0.0000
|2025-01-09 23:34:56| P: 0.4478 ± 0.0000
|2025-01-09 23:34:56| Recall: 0.4735 ± 0.0000
|2025-01-09 23:34:56| train_time: 130.9492 ± 0.0000
|2025-01-09 23:34:56| Flops: 91060736
|2025-01-09 23:34:56| Params: 282693
|2025-01-09 23:34:56| Inference time: 0.46 ms
|2025-01-09 23:34:56| ********************Experiment Success********************
```

