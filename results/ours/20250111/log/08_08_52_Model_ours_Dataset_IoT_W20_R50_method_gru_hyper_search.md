```python
|2025-01-11 08:08:52| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7fd9c74a2390>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 50, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': gru, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 08:08:52| ********************Experiment Start********************
|2025-01-11 08:15:10| Round=1 BestEpoch=122 Acc=0.9168 F1=0.8750 Precision=0.8751 Recall=0.8758 Training_time=267.3 s 

|2025-01-11 08:15:10| ********************Experiment Results:********************
|2025-01-11 08:15:10| Acc: 0.9168 ± 0.0000
|2025-01-11 08:15:10| F1: 0.8750 ± 0.0000
|2025-01-11 08:15:10| P: 0.8751 ± 0.0000
|2025-01-11 08:15:10| Recall: 0.8758 ± 0.0000
|2025-01-11 08:15:10| train_time: 267.2825 ± 0.0000
|2025-01-11 08:15:11| Flops: 233356800
|2025-01-11 08:15:11| Params: 148825
|2025-01-11 08:15:11| Inference time: 0.38 ms
|2025-01-11 08:15:12| ********************Experiment Success********************
```

