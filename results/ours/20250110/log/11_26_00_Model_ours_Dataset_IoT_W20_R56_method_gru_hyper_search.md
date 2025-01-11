```python
|2025-01-10 11:26:00| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x75d68c4ce1e0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 56,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 11:26:00| ********************Experiment Start********************
|2025-01-10 11:31:58| Round=1 BestEpoch=138 Acc=0.9158 F1=0.8742 Precision=0.8764 Recall=0.8740 Training_time=255.7 s 

|2025-01-10 11:31:58| ********************Experiment Results:********************
|2025-01-10 11:31:58| Acc: 0.9158 ± 0.0000
|2025-01-10 11:31:58| F1: 0.8742 ± 0.0000
|2025-01-10 11:31:58| P: 0.8764 ± 0.0000
|2025-01-10 11:31:58| Recall: 0.8740 ± 0.0000
|2025-01-10 11:31:58| train_time: 255.6563 ± 0.0000
|2025-01-10 11:31:59| Flops: 127317120
|2025-01-10 11:31:59| Params: 122493
|2025-01-10 11:31:59| Inference time: 0.39 ms
|2025-01-10 11:32:00| ********************Experiment Success********************
```

