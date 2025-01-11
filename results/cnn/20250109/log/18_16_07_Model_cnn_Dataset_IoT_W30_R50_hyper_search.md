```python
|2025-01-09 18:16:07| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 30,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x77c85ce96450>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': cnn, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 18:16:07| ********************Experiment Start********************
|2025-01-09 18:23:33| Round=1 BestEpoch=401 Acc=0.8471 F1=0.7668 Precision=0.7816 Recall=0.7621 Training_time=325.4 s 

|2025-01-09 18:23:33| ********************Experiment Results:********************
|2025-01-09 18:23:33| Acc: 0.8471 ± 0.0000
|2025-01-09 18:23:33| F1: 0.7668 ± 0.0000
|2025-01-09 18:23:33| P: 0.7816 ± 0.0000
|2025-01-09 18:23:33| Recall: 0.7621 ± 0.0000
|2025-01-09 18:23:33| train_time: 325.3802 ± 0.0000
|2025-01-09 18:23:34| Flops: 31244800
|2025-01-09 18:23:34| Params: 9021
|2025-01-09 18:23:34| Inference time: 0.10 ms
|2025-01-09 18:23:34| ********************Experiment Success********************
```

