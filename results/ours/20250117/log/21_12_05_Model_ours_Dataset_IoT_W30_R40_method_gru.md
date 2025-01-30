```python
|2025-01-17 21:12:05| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x66d3a683950>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-17 21:12:05| ********************Experiment Start********************
|2025-01-17 21:12:06| Acc=0.9038 F1=0.8450 Precision=0.8555 Recall=0.8397 time=186.0 s 
|2025-01-17 21:12:06| ********************Experiment Results:********************
|2025-01-17 21:12:06| Acc: 0.9038 ± 0.0000
|2025-01-17 21:12:06| F1: 0.8450 ± 0.0000
|2025-01-17 21:12:06| P: 0.8555 ± 0.0000
|2025-01-17 21:12:06| Recall: 0.8397 ± 0.0000
|2025-01-17 21:12:06| train_time: 186.0214 ± 0.0000
|2025-01-17 21:12:06| Flops: 661100800
|2025-01-17 21:12:06| Params: 218629
|2025-01-17 21:12:06| Inference time: 0.72 ms
|2025-01-17 21:12:06| ********************Experiment Success********************
```

