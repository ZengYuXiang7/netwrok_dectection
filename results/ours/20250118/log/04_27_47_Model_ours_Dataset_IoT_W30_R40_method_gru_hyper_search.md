```python
|2025-01-18 04:27:47| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x78636a902b70>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 04:27:47| ********************Experiment Start********************
|2025-01-18 05:00:03| Round=1 BestEpoch=124 Acc=0.9010 F1=0.8405 Precision=0.8465 Recall=0.8364 Training_time=1488.4 s 

|2025-01-18 05:00:03| ********************Experiment Results:********************
|2025-01-18 05:00:03| Acc: 0.9010 ± 0.0000
|2025-01-18 05:00:03| F1: 0.8405 ± 0.0000
|2025-01-18 05:00:03| P: 0.8465 ± 0.0000
|2025-01-18 05:00:03| Recall: 0.8364 ± 0.0000
|2025-01-18 05:00:03| train_time: 1488.3971 ± 0.0000
|2025-01-18 05:00:04| Flops: 753982720
|2025-01-18 05:00:04| Params: 429149
|2025-01-18 05:00:04| Inference time: 3.89 ms
|2025-01-18 05:00:04| ********************Experiment Success********************
```

