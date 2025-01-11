```python
|2025-01-10 15:59:21| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x78497f722330>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 15:59:21| ********************Experiment Start********************
|2025-01-10 16:05:12| Round=1 BestEpoch=134 Acc=0.9148 F1=0.8731 Precision=0.8777 Recall=0.8708 Training_time=248.1 s 

|2025-01-10 16:05:12| ********************Experiment Results:********************
|2025-01-10 16:05:12| Acc: 0.9148 ± 0.0000
|2025-01-10 16:05:12| F1: 0.8731 ± 0.0000
|2025-01-10 16:05:12| P: 0.8777 ± 0.0000
|2025-01-10 16:05:12| Recall: 0.8708 ± 0.0000
|2025-01-10 16:05:12| train_time: 248.0608 ± 0.0000
|2025-01-10 16:05:13| Flops: 102028800
|2025-01-10 16:05:13| Params: 98175
|2025-01-10 16:05:13| Inference time: 0.38 ms
|2025-01-10 16:05:13| ********************Experiment Success********************
```

