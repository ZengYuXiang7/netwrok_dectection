```python
|2025-01-09 18:40:36| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'hyper_search': False, 'log': <utils.logger.Logger object at 0xc4f9a11f0e0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': cnn, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 80,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 18:40:36| ********************Experiment Start********************
|2025-01-09 18:40:37| Acc=0.8856 F1=0.8169 Precision=0.8318 Recall=0.8122 time=335.1 s 
|2025-01-09 18:40:37| ********************Experiment Results:********************
|2025-01-09 18:40:37| Acc: 0.8856 ± 0.0000
|2025-01-09 18:40:37| F1: 0.8169 ± 0.0000
|2025-01-09 18:40:37| P: 0.8318 ± 0.0000
|2025-01-09 18:40:37| Recall: 0.8122 ± 0.0000
|2025-01-09 18:40:37| train_time: 335.1290 ± 0.0000
|2025-01-09 18:40:38| Flops: 77639680
|2025-01-09 18:40:38| Params: 21621
|2025-01-09 18:40:38| Inference time: 0.10 ms
|2025-01-09 18:40:38| ********************Experiment Success********************
```

