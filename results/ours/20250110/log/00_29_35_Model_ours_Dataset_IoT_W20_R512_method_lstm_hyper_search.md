```python
|2025-01-10 00:29:35| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x70f204ca6000>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 512,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': lstm, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 00:29:35| ********************Experiment Start********************
|2025-01-10 00:43:32| Round=1 BestEpoch= 79 Acc=0.9018 F1=0.8525 Precision=0.8536 Recall=0.8519 Training_time=573.4 s 

|2025-01-10 00:43:32| ********************Experiment Results:********************
|2025-01-10 00:43:32| Acc: 0.9018 ± 0.0000
|2025-01-10 00:43:32| F1: 0.8525 ± 0.0000
|2025-01-10 00:43:32| P: 0.8536 ± 0.0000
|2025-01-10 00:43:32| Recall: 0.8519 ± 0.0000
|2025-01-10 00:43:32| train_time: 573.3973 ± 0.0000
|2025-01-10 00:43:34| Flops: 12925566976
|2025-01-10 00:43:34| Params: 10920981
|2025-01-10 00:43:34| Inference time: 1.10 ms
|2025-01-10 00:43:35| ********************Experiment Success********************
```

