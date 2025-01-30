```python
|2025-01-18 16:03:12| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x744237b3b500>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 9, 'verbose': 1,
}
|2025-01-18 16:03:12| ********************Experiment Start********************
|2025-01-18 16:19:12| Round=1 BestEpoch=115 Acc=0.9092 F1=0.8473 Precision=0.8533 Recall=0.8435 Training_time=732.1 s 

|2025-01-18 16:19:12| ********************Experiment Results:********************
|2025-01-18 16:19:12| Acc: 0.9092 ± 0.0000
|2025-01-18 16:19:12| F1: 0.8473 ± 0.0000
|2025-01-18 16:19:12| P: 0.8533 ± 0.0000
|2025-01-18 16:19:12| Recall: 0.8435 ± 0.0000
|2025-01-18 16:19:12| train_time: 732.1359 ± 0.0000
|2025-01-18 16:19:13| Flops: 1444320000
|2025-01-18 16:19:13| Params: 1059175
|2025-01-18 16:19:13| Inference time: 1.85 ms
|2025-01-18 16:19:13| ********************Experiment Success********************
```

