```python
|2025-01-09 17:05:53| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x77f871c023f0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': mlp, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 80,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 17:05:53| ********************Experiment Start********************
|2025-01-09 17:10:59| Round=1 BestEpoch=197 Acc=0.7893 F1=0.6949 Precision=0.7281 Recall=0.6761 Training_time=216.1 s 

|2025-01-09 17:10:59| ********************Experiment Results:********************
|2025-01-09 17:10:59| Acc: 0.7893 ± 0.0000
|2025-01-09 17:10:59| F1: 0.6949 ± 0.0000
|2025-01-09 17:10:59| P: 0.7281 ± 0.0000
|2025-01-09 17:10:59| Recall: 0.6761 ± 0.0000
|2025-01-09 17:10:59| train_time: 216.1174 ± 0.0000
|2025-01-09 17:11:00| Flops: 1331712
|2025-01-09 17:11:00| Params: 10223
|2025-01-09 17:11:00| Inference time: 0.05 ms
|2025-01-09 17:11:01| ********************Experiment Success********************
```

