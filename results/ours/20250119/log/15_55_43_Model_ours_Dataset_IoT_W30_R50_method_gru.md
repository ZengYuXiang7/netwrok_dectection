```python
|2025-01-19 15:55:43| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x7f693187230>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 15:55:43| ********************Experiment Start********************
|2025-01-19 15:55:44| Acc=0.9192 F1=0.8593 Precision=0.8615 Recall=0.8578 time=162.1 s 
|2025-01-19 15:55:44| ********************Experiment Results:********************
|2025-01-19 15:55:44| Acc: 0.9192 ± 0.0000
|2025-01-19 15:55:44| F1: 0.8593 ± 0.0000
|2025-01-19 15:55:44| P: 0.8615 ± 0.0000
|2025-01-19 15:55:44| Recall: 0.8578 ± 0.0000
|2025-01-19 15:55:44| train_time: 162.0699 ± 0.0000
|2025-01-19 15:55:44| Flops: 686284800
|2025-01-19 15:55:44| Params: 253275
|2025-01-19 15:55:44| Inference time: 0.51 ms
|2025-01-19 15:55:44| ********************Experiment Success********************
```

