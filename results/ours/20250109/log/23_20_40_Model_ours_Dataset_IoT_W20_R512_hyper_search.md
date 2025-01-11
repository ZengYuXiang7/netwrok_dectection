```python
|2025-01-09 23:20:40| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x730ea5829be0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 512,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': lstm, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:20:40| ********************Experiment Start********************
|2025-01-09 23:34:39| Round=1 BestEpoch= 79 Acc=0.9018 F1=0.8525 Precision=0.8536 Recall=0.8519 Training_time=574.8 s 

|2025-01-09 23:34:39| ********************Experiment Results:********************
|2025-01-09 23:34:39| Acc: 0.9018 ± 0.0000
|2025-01-09 23:34:39| F1: 0.8525 ± 0.0000
|2025-01-09 23:34:39| P: 0.8536 ± 0.0000
|2025-01-09 23:34:39| Recall: 0.8519 ± 0.0000
|2025-01-09 23:34:39| train_time: 574.7676 ± 0.0000
|2025-01-09 23:34:41| Flops: 12925566976
|2025-01-09 23:34:41| Params: 10920981
|2025-01-09 23:34:41| Inference time: 1.10 ms
|2025-01-09 23:34:42| ********************Experiment Success********************
```

