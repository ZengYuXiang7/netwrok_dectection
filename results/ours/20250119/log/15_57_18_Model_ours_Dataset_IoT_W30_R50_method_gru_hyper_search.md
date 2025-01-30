```python
|2025-01-19 15:57:18| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7ea54b91a420>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 15:57:18| ********************Experiment Start********************
|2025-01-19 16:06:12| Round=1 BestEpoch= 51 Acc=0.9161 F1=0.8551 Precision=0.8580 Recall=0.8540 Training_time=322.8 s 

|2025-01-19 16:06:12| ********************Experiment Results:********************
|2025-01-19 16:06:12| Acc: 0.9161 ± 0.0000
|2025-01-19 16:06:12| F1: 0.8551 ± 0.0000
|2025-01-19 16:06:12| P: 0.8580 ± 0.0000
|2025-01-19 16:06:12| Recall: 0.8540 ± 0.0000
|2025-01-19 16:06:12| train_time: 322.7947 ± 0.0000
|2025-01-19 16:06:13| Flops: 1444320000
|2025-01-19 16:06:13| Params: 1059175
|2025-01-19 16:06:13| Inference time: 1.87 ms
|2025-01-19 16:06:13| ********************Experiment Success********************
```

