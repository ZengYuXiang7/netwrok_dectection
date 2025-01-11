```python
|2025-01-08 20:44:35| {
     'Ablation': 0, 'bs': 256, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 200, 'eval_set': True, 'experiment': False, 'log': <utils.logger.Logger object at 0x68b11476c90>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 50, 'record': True, 'retrain': False,
     'rounds': 1, 'seed': 0, 'time_interval': 10, 'train_size': 500,
     'verbose': 0,
}
|2025-01-08 20:44:35| ********************Experiment Start********************
|2025-01-08 20:46:29| Round=1 BestEpoch=  1 Acc=0.0425 F1=0.0039 Precision=0.0020 Recall=0.0476 Training_time=3.1 s 

|2025-01-08 20:46:29| ********************Experiment Results:********************
|2025-01-08 20:46:29| Acc: 0.0425 ± 0.0000
|2025-01-08 20:46:29| F1: 0.0039 ± 0.0000
|2025-01-08 20:46:29| P: 0.0020 ± 0.0000
|2025-01-08 20:46:29| Recall: 0.0476 ± 0.0000
|2025-01-08 20:46:29| train_time: 3.0677 ± 0.0000
|2025-01-08 20:46:33| Flops: 98278400
|2025-01-08 20:46:33| Params: 383525
|2025-01-08 20:46:33| Inference time: 0.32 ms
|2025-01-08 20:46:33| ********************Experiment Success********************
```

