```python
|2025-01-17 20:52:37| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x1298acc63110>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 64, 'record': True, 'retrain': False, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-17 20:52:37| ********************Experiment Start********************
|2025-01-17 20:52:38| Acc=0.8412 F1=0.7615 Precision=0.7662 Recall=0.7582 time=111.6 s 
|2025-01-17 20:52:38| ********************Experiment Results:********************
|2025-01-17 20:52:38| Acc: 0.8412 ± 0.0000
|2025-01-17 20:52:38| F1: 0.7615 ± 0.0000
|2025-01-17 20:52:38| P: 0.7662 ± 0.0000
|2025-01-17 20:52:38| Recall: 0.7582 ± 0.0000
|2025-01-17 20:52:38| train_time: 111.6228 ± 0.0000
|2025-01-17 20:52:38| Flops: 202752000
|2025-01-17 20:52:38| Params: 90773
|2025-01-17 20:52:38| Inference time: 0.08 ms
|2025-01-17 20:52:38| ********************Experiment Success********************
```

