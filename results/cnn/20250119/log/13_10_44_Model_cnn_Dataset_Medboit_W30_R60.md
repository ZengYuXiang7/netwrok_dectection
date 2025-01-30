```python
|2025-01-19 13:10:44| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xbad02c903e0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': cnn, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 13:10:44| ********************Experiment Start********************
|2025-01-19 13:10:45| Acc=0.7150 F1=0.6084 Precision=0.6432 Recall=0.5953 time=44.9 s 
|2025-01-19 13:10:45| Acc=0.7378 F1=0.6865 Precision=0.6934 Recall=0.6850 time=33.5 s 
|2025-01-19 13:10:45| Acc=0.7358 F1=0.6381 Precision=0.6875 Recall=0.6272 time=31.9 s 
|2025-01-19 13:10:45| Acc=0.6832 F1=0.5904 Precision=0.6606 Recall=0.5649 time=21.0 s 
|2025-01-19 13:10:45| Acc=0.7577 F1=0.6940 Precision=0.7094 Recall=0.6888 time=47.4 s 
|2025-01-19 13:10:45| ********************Experiment Results:********************
|2025-01-19 13:10:45| Acc: 0.7259 ± 0.0253
|2025-01-19 13:10:45| F1: 0.6435 ± 0.0412
|2025-01-19 13:10:45| P: 0.6788 ± 0.0238
|2025-01-19 13:10:45| Recall: 0.6322 ± 0.0488
|2025-01-19 13:10:45| train_time: 35.7272 ± 9.5377
|2025-01-19 13:10:45| Flops: 44305920
|2025-01-19 13:10:45| Params: 11828
|2025-01-19 13:10:45| Inference time: 0.10 ms
|2025-01-19 13:10:45| ********************Experiment Success********************
```

