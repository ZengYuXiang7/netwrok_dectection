```python
|2025-01-19 12:53:42| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0xde0649337a0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 60, 'record': True, 'retrain': False, 'rounds': 5,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 12:53:42| ********************Experiment Start********************
|2025-01-19 12:53:43| Acc=0.7339 F1=0.6683 Precision=0.6690 Recall=0.6686 time=31.0 s 
|2025-01-19 12:53:43| Acc=0.7428 F1=0.6790 Precision=0.6877 Recall=0.6805 time=12.3 s 
|2025-01-19 12:53:43| Acc=0.7299 F1=0.6770 Precision=0.6823 Recall=0.6745 time=16.0 s 
|2025-01-19 12:53:43| Acc=0.7428 F1=0.6837 Precision=0.6884 Recall=0.6800 time=29.5 s 
|2025-01-19 12:53:43| Acc=0.7637 F1=0.6914 Precision=0.6847 Recall=0.7031 time=17.7 s 
|2025-01-19 12:53:43| ********************Experiment Results:********************
|2025-01-19 12:53:43| Acc: 0.7426 ± 0.0117
|2025-01-19 12:53:43| F1: 0.6799 ± 0.0076
|2025-01-19 12:53:43| P: 0.6824 ± 0.0071
|2025-01-19 12:53:43| Recall: 0.6813 ± 0.0117
|2025-01-19 12:53:43| train_time: 21.3011 ± 7.5266
|2025-01-19 12:53:44| Flops: 176025600
|2025-01-19 12:53:44| Params: 58808
|2025-01-19 12:53:44| Inference time: 0.08 ms
|2025-01-19 12:53:44| ********************Experiment Success********************
```

