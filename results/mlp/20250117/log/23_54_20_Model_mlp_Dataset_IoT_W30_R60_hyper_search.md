```python
|2025-01-17 23:54:20| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x799dae19ecc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': mlp, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-17 23:54:20| ********************Experiment Start********************
|2025-01-17 23:57:02| Round=1 BestEpoch=220 Acc=0.7438 F1=0.6351 Precision=0.6931 Recall=0.6281 Training_time=115.1 s 

|2025-01-17 23:57:02| ********************Experiment Results:********************
|2025-01-17 23:57:02| Acc: 0.7438 ± 0.0000
|2025-01-17 23:57:02| F1: 0.6351 ± 0.0000
|2025-01-17 23:57:02| P: 0.6931 ± 0.0000
|2025-01-17 23:57:02| Recall: 0.6281 ± 0.0000
|2025-01-17 23:57:02| train_time: 115.1288 ± 0.0000
|2025-01-17 23:57:02| Flops: 924672
|2025-01-17 23:57:02| Params: 7083
|2025-01-17 23:57:02| Inference time: 0.05 ms
|2025-01-17 23:57:03| ********************Experiment Success********************
```

