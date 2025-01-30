```python
|2025-01-18 22:57:46| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x75d066bcecc0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 22:57:46| ********************Experiment Start********************
|2025-01-18 22:58:27| Round=1 BestEpoch= 64 Acc=0.9341 F1=0.7413 Precision=0.7395 Recall=0.7484 Training_time=21.3 s 

|2025-01-18 22:58:27| ********************Experiment Results:********************
|2025-01-18 22:58:27| Acc: 0.9341 ± 0.0000
|2025-01-18 22:58:27| F1: 0.7413 ± 0.0000
|2025-01-18 22:58:27| P: 0.7395 ± 0.0000
|2025-01-18 22:58:27| Recall: 0.7484 ± 0.0000
|2025-01-18 22:58:27| train_time: 21.3189 ± 0.0000
|2025-01-18 22:58:28| Flops: 176025600
|2025-01-18 22:58:28| Params: 58808
|2025-01-18 22:58:28| Inference time: 0.09 ms
|2025-01-18 22:58:28| ********************Experiment Success********************
```

