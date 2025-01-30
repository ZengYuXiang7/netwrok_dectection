```python
|2025-01-18 22:56:32| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c2089b29010>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-18 22:56:32| ********************Experiment Start********************
|2025-01-18 22:57:43| Round=1 BestEpoch=136 Acc=0.9401 F1=0.7414 Precision=0.7503 Recall=0.7333 Training_time=44.8 s 

|2025-01-18 22:57:43| ********************Experiment Results:********************
|2025-01-18 22:57:43| Acc: 0.9401 ± 0.0000
|2025-01-18 22:57:43| F1: 0.7414 ± 0.0000
|2025-01-18 22:57:43| P: 0.7503 ± 0.0000
|2025-01-18 22:57:43| Recall: 0.7333 ± 0.0000
|2025-01-18 22:57:43| train_time: 44.7884 ± 0.0000
|2025-01-18 22:57:44| Flops: 123648000
|2025-01-18 22:57:44| Params: 43008
|2025-01-18 22:57:44| Inference time: 0.07 ms
|2025-01-18 22:57:44| ********************Experiment Success********************
```

