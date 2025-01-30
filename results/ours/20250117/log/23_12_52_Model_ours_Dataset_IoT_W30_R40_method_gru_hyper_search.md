```python
|2025-01-17 23:12:52| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b7b42e8a4b0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-17 23:12:52| ********************Experiment Start********************
|2025-01-17 23:23:37| Round=1 BestEpoch=124 Acc=0.9010 F1=0.8405 Precision=0.8465 Recall=0.8364 Training_time=494.4 s 

|2025-01-17 23:23:37| ********************Experiment Results:********************
|2025-01-17 23:23:37| Acc: 0.9010 ± 0.0000
|2025-01-17 23:23:37| F1: 0.8405 ± 0.0000
|2025-01-17 23:23:37| P: 0.8465 ± 0.0000
|2025-01-17 23:23:37| Recall: 0.8364 ± 0.0000
|2025-01-17 23:23:37| train_time: 494.3789 ± 0.0000
|2025-01-17 23:23:37| Flops: 753982720
|2025-01-17 23:23:37| Params: 429149
|2025-01-17 23:23:37| Inference time: 1.12 ms
|2025-01-17 23:23:38| ********************Experiment Success********************
```

