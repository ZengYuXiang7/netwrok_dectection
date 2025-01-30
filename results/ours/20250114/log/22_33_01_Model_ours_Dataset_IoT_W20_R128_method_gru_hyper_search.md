```python
|2025-01-14 22:33:01| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x79fa2485ab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-14 22:33:01| ********************Experiment Start********************
|2025-01-14 23:20:55| Round=1 BestEpoch=155 Acc=0.9244 F1=0.8845 Precision=0.8837 Recall=0.8859 Training_time=2318.1 s 

|2025-01-14 23:20:55| ********************Experiment Results:********************
|2025-01-14 23:20:55| Acc: 0.9244 ± 0.0000
|2025-01-14 23:20:55| F1: 0.8845 ± 0.0000
|2025-01-14 23:20:55| P: 0.8837 ± 0.0000
|2025-01-14 23:20:55| Recall: 0.8859 ± 0.0000
|2025-01-14 23:20:55| train_time: 2318.0941 ± 0.0000
|2025-01-14 23:20:56| Flops: 8989855744
|2025-01-14 23:20:56| Params: 9182549
|2025-01-14 23:20:56| Inference time: 2.43 ms
|2025-01-14 23:20:57| ********************Experiment Success********************
```

