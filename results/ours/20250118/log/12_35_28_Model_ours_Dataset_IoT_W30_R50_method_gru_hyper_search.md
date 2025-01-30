```python
|2025-01-18 12:35:28| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7bbb1dd1f260>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 12:35:28| ********************Experiment Start********************
|2025-01-18 12:44:22| Round=1 BestEpoch= 72 Acc=0.9028 F1=0.8330 Precision=0.8397 Recall=0.8302 Training_time=360.9 s 

|2025-01-18 12:44:22| ********************Experiment Results:********************
|2025-01-18 12:44:22| Acc: 0.9028 ± 0.0000
|2025-01-18 12:44:22| F1: 0.8330 ± 0.0000
|2025-01-18 12:44:22| P: 0.8397 ± 0.0000
|2025-01-18 12:44:22| Recall: 0.8302 ± 0.0000
|2025-01-18 12:44:22| train_time: 360.8976 ± 0.0000
|2025-01-18 12:44:22| Flops: 1234790400
|2025-01-18 12:44:22| Params: 833025
|2025-01-18 12:44:22| Inference time: 1.42 ms
|2025-01-18 12:44:23| ********************Experiment Success********************
```

