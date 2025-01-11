```python
|2025-01-11 08:57:26| {
     'Ablation': 0, 'bidirectional': False, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d4e536decc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 128, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': gru, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 08:57:26| ********************Experiment Start********************
|2025-01-11 09:01:15| Round=1 BestEpoch= 70 Acc=0.9150 F1=0.8747 Precision=0.8718 Recall=0.8788 Training_time=139.6 s 

|2025-01-11 09:01:15| ********************Experiment Results:********************
|2025-01-11 09:01:15| Acc: 0.9150 ± 0.0000
|2025-01-11 09:01:15| F1: 0.8747 ± 0.0000
|2025-01-11 09:01:15| P: 0.8718 ± 0.0000
|2025-01-11 09:01:15| Recall: 0.8788 ± 0.0000
|2025-01-11 09:01:15| train_time: 139.5503 ± 0.0000
|2025-01-11 09:01:17| Flops: 649072640
|2025-01-11 09:01:17| Params: 625877
|2025-01-11 09:01:17| Inference time: 0.33 ms
|2025-01-11 09:01:18| ********************Experiment Success********************
```

