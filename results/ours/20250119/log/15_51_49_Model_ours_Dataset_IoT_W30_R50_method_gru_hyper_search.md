```python
|2025-01-19 15:51:49| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e3e96dba8a0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 15:51:49| ********************Experiment Start********************
|2025-01-19 15:55:41| Round=1 BestEpoch=102 Acc=0.9222 F1=0.8629 Precision=0.8682 Recall=0.8588 Training_time=162.1 s 

|2025-01-19 15:55:41| ********************Experiment Results:********************
|2025-01-19 15:55:41| Acc: 0.9222 ± 0.0000
|2025-01-19 15:55:41| F1: 0.8629 ± 0.0000
|2025-01-19 15:55:41| P: 0.8682 ± 0.0000
|2025-01-19 15:55:41| Recall: 0.8588 ± 0.0000
|2025-01-19 15:55:41| train_time: 162.0699 ± 0.0000
|2025-01-19 15:55:41| Flops: 686284800
|2025-01-19 15:55:41| Params: 253275
|2025-01-19 15:55:41| Inference time: 0.40 ms
|2025-01-19 15:55:41| ********************Experiment Success********************
```

