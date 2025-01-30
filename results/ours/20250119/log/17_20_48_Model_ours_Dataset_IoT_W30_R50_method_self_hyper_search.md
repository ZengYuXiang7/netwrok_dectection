```python
|2025-01-19 17:20:48| {
     'Ablation': 0, 'bidirectional': False, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x784a86d50320>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': self,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 17:20:48| ********************Experiment Start********************
|2025-01-19 17:24:41| Round=1 BestEpoch=153 Acc=0.9003 F1=0.8263 Precision=0.8303 Recall=0.8253 Training_time=172.1 s 

|2025-01-19 17:24:41| ********************Experiment Results:********************
|2025-01-19 17:24:41| Acc: 0.9003 ± 0.0000
|2025-01-19 17:24:41| F1: 0.8263 ± 0.0000
|2025-01-19 17:24:41| P: 0.8303 ± 0.0000
|2025-01-19 17:24:41| Recall: 0.8253 ± 0.0000
|2025-01-19 17:24:41| train_time: 172.1287 ± 0.0000
|2025-01-19 17:24:41| Flops: 51916800
|2025-01-19 17:24:41| Params: 90775
|2025-01-19 17:24:41| Inference time: 0.39 ms
|2025-01-19 17:24:41| ********************Experiment Success********************
```

