```python
|2025-01-11 09:41:30| {
     'Ablation': 0, 'bidirectional': False, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b719e831880>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 100, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': lstm, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 09:41:30| ********************Experiment Start********************
|2025-01-11 09:47:08| Round=1 BestEpoch=116 Acc=0.9145 F1=0.8734 Precision=0.8750 Recall=0.8727 Training_time=233.8 s 

|2025-01-11 09:47:08| ********************Experiment Results:********************
|2025-01-11 09:47:08| Acc: 0.9145 ± 0.0000
|2025-01-11 09:47:08| F1: 0.8734 ± 0.0000
|2025-01-11 09:47:08| P: 0.8750 ± 0.0000
|2025-01-11 09:47:08| Recall: 0.8727 ± 0.0000
|2025-01-11 09:47:08| train_time: 233.7545 ± 0.0000
|2025-01-11 09:47:09| Flops: 502204800
|2025-01-11 09:47:09| Params: 424021
|2025-01-11 09:47:09| Inference time: 0.32 ms
|2025-01-11 09:47:09| ********************Experiment Success********************
```

