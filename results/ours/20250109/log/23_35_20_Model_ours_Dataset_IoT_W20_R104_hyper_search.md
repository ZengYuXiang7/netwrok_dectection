```python
|2025-01-09 23:35:20| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7271724de780>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 104,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': external, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:35:20| ********************Experiment Start********************
|2025-01-09 23:35:21| Acc=0.5913 F1=0.5161 Precision=0.5643 Recall=0.5594 time=130.9 s 
|2025-01-09 23:35:21| ********************Experiment Results:********************
|2025-01-09 23:35:21| Acc: 0.5913 ± 0.0000
|2025-01-09 23:35:21| F1: 0.5161 ± 0.0000
|2025-01-09 23:35:21| P: 0.5643 ± 0.0000
|2025-01-09 23:35:21| Recall: 0.5594 ± 0.0000
|2025-01-09 23:35:21| train_time: 130.9492 ± 0.0000
|2025-01-09 23:35:22| Flops: 160184832
|2025-01-09 23:35:22| Params: 309317
|2025-01-09 23:35:22| Inference time: 0.37 ms
|2025-01-09 23:35:22| ********************Experiment Success********************
```

