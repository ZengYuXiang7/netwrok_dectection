```python
|2025-01-13 18:16:15| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x79f39d902b10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 16, 'verbose': 10,
}
|2025-01-13 18:16:15| ********************Experiment Start********************
|2025-01-13 18:33:26| Round=1 BestEpoch=182 Acc=0.9241 F1=0.8862 Precision=0.8874 Recall=0.8859 Training_time=805.7 s 

|2025-01-13 18:33:26| ********************Experiment Results:********************
|2025-01-13 18:33:26| Acc: 0.9241 ± 0.0000
|2025-01-13 18:33:26| F1: 0.8862 ± 0.0000
|2025-01-13 18:33:26| P: 0.8874 ± 0.0000
|2025-01-13 18:33:26| Recall: 0.8859 ± 0.0000
|2025-01-13 18:33:26| train_time: 805.7022 ± 0.0000
|2025-01-13 18:33:29| Flops: 4387180544
|2025-01-13 18:33:29| Params: 2058965
|2025-01-13 18:33:29| Inference time: 0.79 ms
|2025-01-13 18:33:30| ********************Experiment Success********************
```

