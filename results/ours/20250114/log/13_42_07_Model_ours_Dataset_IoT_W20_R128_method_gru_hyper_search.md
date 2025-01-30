```python
|2025-01-14 13:42:07| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a29ca6c6cc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 13:42:07| ********************Experiment Start********************
|2025-01-14 13:54:27| Round=1 BestEpoch=121 Acc=0.9254 F1=0.8864 Precision=0.8866 Recall=0.8867 Training_time=534.2 s 

|2025-01-14 13:54:27| ********************Experiment Results:********************
|2025-01-14 13:54:27| Acc: 0.9254 ± 0.0000
|2025-01-14 13:54:27| F1: 0.8864 ± 0.0000
|2025-01-14 13:54:27| P: 0.8866 ± 0.0000
|2025-01-14 13:54:27| Recall: 0.8867 ± 0.0000
|2025-01-14 13:54:27| train_time: 534.1994 ± 0.0000
|2025-01-14 13:54:28| Flops: 4384100352
|2025-01-14 13:54:28| Params: 2047445
|2025-01-14 13:54:28| Inference time: 0.68 ms
|2025-01-14 13:54:28| ********************Experiment Success********************
```

