```python
|2025-01-14 22:02:34| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7608da423620>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-14 22:02:34| ********************Experiment Start********************
|2025-01-14 22:14:29| Round=1 BestEpoch=124 Acc=0.9272 F1=0.8918 Precision=0.8930 Recall=0.8911 Training_time=517.0 s 

|2025-01-14 22:14:29| ********************Experiment Results:********************
|2025-01-14 22:14:29| Acc: 0.9272 ± 0.0000
|2025-01-14 22:14:29| F1: 0.8918 ± 0.0000
|2025-01-14 22:14:29| P: 0.8930 ± 0.0000
|2025-01-14 22:14:29| Recall: 0.8911 ± 0.0000
|2025-01-14 22:14:29| train_time: 516.9784 ± 0.0000
|2025-01-14 22:14:30| Flops: 4383051776
|2025-01-14 22:14:30| Params: 2039125
|2025-01-14 22:14:30| Inference time: 0.52 ms
|2025-01-14 22:14:30| ********************Experiment Success********************
```

