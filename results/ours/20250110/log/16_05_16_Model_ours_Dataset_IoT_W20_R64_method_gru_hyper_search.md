```python
|2025-01-10 16:05:16| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x74ce78bac530>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 16:05:16| ********************Experiment Start********************
|2025-01-10 16:12:01| Round=1 BestEpoch=159 Acc=0.9168 F1=0.8771 Precision=0.8814 Recall=0.8750 Training_time=295.2 s 

|2025-01-10 16:12:01| ********************Experiment Results:********************
|2025-01-10 16:12:01| Acc: 0.9168 ± 0.0000
|2025-01-10 16:12:01| F1: 0.8771 ± 0.0000
|2025-01-10 16:12:01| P: 0.8814 ± 0.0000
|2025-01-10 16:12:01| Recall: 0.8750 ± 0.0000
|2025-01-10 16:12:01| train_time: 295.1873 ± 0.0000
|2025-01-10 16:12:02| Flops: 165385856
|2025-01-10 16:12:02| Params: 159117
|2025-01-10 16:12:02| Inference time: 0.40 ms
|2025-01-10 16:12:02| ********************Experiment Success********************
```

