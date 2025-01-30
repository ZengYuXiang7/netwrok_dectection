```python
|2025-01-19 17:25:01| {
     'Ablation': 0, 'bidirectional': False, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a3f13482450>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': self,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 17:25:01| ********************Experiment Start********************
|2025-01-19 17:30:57| Round=1 BestEpoch=250 Acc=0.9083 F1=0.8444 Precision=0.8551 Recall=0.8399 Training_time=281.7 s 

|2025-01-19 17:30:57| ********************Experiment Results:********************
|2025-01-19 17:30:57| Acc: 0.9083 ± 0.0000
|2025-01-19 17:30:57| F1: 0.8444 ± 0.0000
|2025-01-19 17:30:57| P: 0.8551 ± 0.0000
|2025-01-19 17:30:57| Recall: 0.8399 ± 0.0000
|2025-01-19 17:30:57| train_time: 281.7007 ± 0.0000
|2025-01-19 17:30:57| Flops: 51916800
|2025-01-19 17:30:57| Params: 90775
|2025-01-19 17:30:57| Inference time: 0.40 ms
|2025-01-19 17:30:57| ********************Experiment Success********************
```

