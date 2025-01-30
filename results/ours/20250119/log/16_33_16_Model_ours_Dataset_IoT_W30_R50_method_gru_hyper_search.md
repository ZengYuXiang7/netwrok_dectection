```python
|2025-01-19 16:33:16| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7f60145c7350>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 16:33:16| ********************Experiment Start********************
|2025-01-19 16:41:05| Round=1 BestEpoch= 48 Acc=0.9094 F1=0.8496 Precision=0.8535 Recall=0.8471 Training_time=276.8 s 

|2025-01-19 16:41:05| ********************Experiment Results:********************
|2025-01-19 16:41:05| Acc: 0.9094 ± 0.0000
|2025-01-19 16:41:05| F1: 0.8496 ± 0.0000
|2025-01-19 16:41:05| P: 0.8535 ± 0.0000
|2025-01-19 16:41:05| Recall: 0.8471 ± 0.0000
|2025-01-19 16:41:05| train_time: 276.8450 ± 0.0000
|2025-01-19 16:41:05| Flops: 1441760000
|2025-01-19 16:41:05| Params: 1038775
|2025-01-19 16:41:05| Inference time: 1.67 ms
|2025-01-19 16:41:06| ********************Experiment Success********************
```

