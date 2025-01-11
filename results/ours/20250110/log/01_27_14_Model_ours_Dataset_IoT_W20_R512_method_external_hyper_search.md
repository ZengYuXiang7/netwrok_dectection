```python
|2025-01-10 01:27:14| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c80e6586cc0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 512,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': external, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 01:27:14| ********************Experiment Start********************
|2025-01-10 01:29:33| Round=1 BestEpoch= 42 Acc=0.8936 F1=0.8366 Precision=0.8432 Recall=0.8312 Training_time=69.4 s 

|2025-01-10 01:29:33| ********************Experiment Results:********************
|2025-01-10 01:29:33| Acc: 0.8936 ± 0.0000
|2025-01-10 01:29:33| F1: 0.8366 ± 0.0000
|2025-01-10 01:29:33| P: 0.8432 ± 0.0000
|2025-01-10 01:29:33| Recall: 0.8312 ± 0.0000
|2025-01-10 01:29:33| train_time: 69.3996 ± 0.0000
|2025-01-10 01:29:34| Flops: 2482716672
|2025-01-10 01:29:34| Params: 6849557
|2025-01-10 01:29:34| Inference time: 0.30 ms
|2025-01-10 01:29:34| ********************Experiment Success********************
```

