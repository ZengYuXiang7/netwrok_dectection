```python
|2025-01-11 08:21:55| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7fcf110e9520>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 100, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': gru, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 08:21:55| ********************Experiment Start********************
|2025-01-11 08:28:49| Round=1 BestEpoch=134 Acc=0.9209 F1=0.8823 Precision=0.8840 Recall=0.8816 Training_time=297.1 s 

|2025-01-11 08:28:49| ********************Experiment Results:********************
|2025-01-11 08:28:49| Acc: 0.9209 ± 0.0000
|2025-01-11 08:28:49| F1: 0.8823 ± 0.0000
|2025-01-11 08:28:49| P: 0.8840 ± 0.0000
|2025-01-11 08:28:49| Recall: 0.8816 ± 0.0000
|2025-01-11 08:28:49| train_time: 297.1460 ± 0.0000
|2025-01-11 08:28:50| Flops: 916924800
|2025-01-11 08:28:50| Params: 584921
|2025-01-11 08:28:50| Inference time: 0.37 ms
|2025-01-11 08:28:51| ********************Experiment Success********************
```

