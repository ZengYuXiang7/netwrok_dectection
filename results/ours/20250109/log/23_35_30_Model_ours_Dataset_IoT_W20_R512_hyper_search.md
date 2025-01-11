```python
|2025-01-09 23:35:30| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7423ddfb1cd0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 512,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': external, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:35:30| ********************Experiment Start********************
|2025-01-09 23:35:32| Acc=0.8629 F1=0.7896 Precision=0.7975 Recall=0.7914 time=574.8 s 
|2025-01-09 23:35:32| ********************Experiment Results:********************
|2025-01-09 23:35:32| Acc: 0.8629 ± 0.0000
|2025-01-09 23:35:32| F1: 0.7896 ± 0.0000
|2025-01-09 23:35:32| P: 0.7975 ± 0.0000
|2025-01-09 23:35:32| Recall: 0.7914 ± 0.0000
|2025-01-09 23:35:32| train_time: 574.7676 ± 0.0000
|2025-01-09 23:35:32| Flops: 2482716672
|2025-01-09 23:35:32| Params: 6849557
|2025-01-09 23:35:32| Inference time: 0.37 ms
|2025-01-09 23:35:32| ********************Experiment Success********************
```

