```python
|2025-01-09 16:55:04| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 1, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x79e2a6d307a0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': mlp, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 16:55:04| ********************Experiment Start********************
|2025-01-09 16:55:07| Round=1 BestEpoch=  1 Acc=0.7605 F1=0.6520 Precision=0.6744 Recall=0.6413 Training_time=1.2 s 

|2025-01-09 16:55:07| ********************Experiment Results:********************
|2025-01-09 16:55:07| Acc: 0.7605 ± 0.0000
|2025-01-09 16:55:07| F1: 0.6520 ± 0.0000
|2025-01-09 16:55:07| P: 0.6744 ± 0.0000
|2025-01-09 16:55:07| Recall: 0.6413 ± 0.0000
|2025-01-09 16:55:07| train_time: 1.1500 ± 0.0000
|2025-01-09 16:55:08| Flops: 644352
|2025-01-09 16:55:08| Params: 4913
|2025-01-09 16:55:08| Inference time: 0.06 ms
|2025-01-09 16:55:08| ********************Experiment Success********************
```

