```python
|2025-01-11 09:07:59| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x757ca6796ed0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 64, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': lstm, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 09:07:59| ********************Experiment Start********************
|2025-01-11 09:16:09| Round=1 BestEpoch=159 Acc=0.9191 F1=0.8777 Precision=0.8809 Recall=0.8754 Training_time=364.8 s 

|2025-01-11 09:16:09| ********************Experiment Results:********************
|2025-01-11 09:16:09| Acc: 0.9191 ± 0.0000
|2025-01-11 09:16:09| F1: 0.8777 ± 0.0000
|2025-01-11 09:16:09| P: 0.8809 ± 0.0000
|2025-01-11 09:16:09| Recall: 0.8754 ± 0.0000
|2025-01-11 09:16:09| train_time: 364.7877 ± 0.0000
|2025-01-11 09:16:10| Flops: 486184576
|2025-01-11 09:16:10| Params: 283341
|2025-01-11 09:16:10| Inference time: 0.37 ms
|2025-01-11 09:16:10| ********************Experiment Success********************
```

