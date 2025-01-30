```python
|2025-01-19 06:20:26| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7f897b8cee70>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 06:20:26| ********************Experiment Start********************
|2025-01-19 06:28:51| Round=1 BestEpoch= 51 Acc=0.9161 F1=0.8551 Precision=0.8580 Recall=0.8540 Training_time=304.9 s 

|2025-01-19 06:28:51| ********************Experiment Results:********************
|2025-01-19 06:28:51| Acc: 0.9161 ± 0.0000
|2025-01-19 06:28:51| F1: 0.8551 ± 0.0000
|2025-01-19 06:28:51| P: 0.8580 ± 0.0000
|2025-01-19 06:28:51| Recall: 0.8540 ± 0.0000
|2025-01-19 06:28:51| train_time: 304.9349 ± 0.0000
|2025-01-19 06:28:51| Flops: 1444320000
|2025-01-19 06:28:51| Params: 1059175
|2025-01-19 06:28:51| Inference time: 1.82 ms
|2025-01-19 06:28:51| ********************Experiment Success********************
```

