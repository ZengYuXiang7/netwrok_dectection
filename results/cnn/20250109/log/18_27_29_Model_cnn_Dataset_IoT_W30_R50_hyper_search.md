```python
|2025-01-09 18:27:29| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7f33c98f1cd0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': cnn, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 18:27:29| ********************Experiment Start********************
|2025-01-09 18:27:30| Acc=0.8471 F1=0.7668 Precision=0.7816 Recall=0.7621 time=325.4 s 
|2025-01-09 18:27:30| ********************Experiment Results:********************
|2025-01-09 18:27:30| Acc: 0.8471 ± 0.0000
|2025-01-09 18:27:30| F1: 0.7668 ± 0.0000
|2025-01-09 18:27:30| P: 0.7816 ± 0.0000
|2025-01-09 18:27:30| Recall: 0.7621 ± 0.0000
|2025-01-09 18:27:30| train_time: 325.3802 ± 0.0000
|2025-01-09 18:27:31| Flops: 31244800
|2025-01-09 18:27:31| Params: 9021
|2025-01-09 18:27:31| Inference time: 0.16 ms
|2025-01-09 18:27:31| ********************Experiment Success********************
```

