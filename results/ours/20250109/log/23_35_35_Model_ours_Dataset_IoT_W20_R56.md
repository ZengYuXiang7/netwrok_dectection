```python
|2025-01-09 23:35:35| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': False, 'log': <utils.logger.Logger object at 0x8ec8adea930>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 56,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': lstm, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:35:35| ********************Experiment Start********************
|2025-01-09 23:35:37| Acc=0.9009 F1=0.8491 Precision=0.8494 Recall=0.8498 time=394.0 s 
|2025-01-09 23:35:37| ********************Experiment Results:********************
|2025-01-09 23:35:37| Acc: 0.9009 ± 0.0000
|2025-01-09 23:35:37| F1: 0.8491 ± 0.0000
|2025-01-09 23:35:37| P: 0.8494 ± 0.0000
|2025-01-09 23:35:37| Recall: 0.8498 ± 0.0000
|2025-01-09 23:35:37| train_time: 393.9708 ± 0.0000
|2025-01-09 23:35:38| Flops: 160222720
|2025-01-09 23:35:38| Params: 134757
|2025-01-09 23:35:38| Inference time: 0.42 ms
|2025-01-09 23:35:38| ********************Experiment Success********************
```

