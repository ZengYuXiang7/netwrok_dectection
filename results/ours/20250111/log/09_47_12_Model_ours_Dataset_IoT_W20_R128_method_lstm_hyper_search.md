```python
|2025-01-11 09:47:12| {
     'Ablation': 0, 'bidirectional': False, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x72231d643170>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 128, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': lstm, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 09:47:12| ********************Experiment Start********************
|2025-01-11 09:53:16| Round=1 BestEpoch=127 Acc=0.9158 F1=0.8737 Precision=0.8747 Recall=0.8733 Training_time=256.3 s 

|2025-01-11 09:53:16| ********************Experiment Results:********************
|2025-01-11 09:53:16| Acc: 0.9158 ± 0.0000
|2025-01-11 09:53:16| F1: 0.8737 ± 0.0000
|2025-01-11 09:53:16| P: 0.8747 ± 0.0000
|2025-01-11 09:53:16| Recall: 0.8733 ± 0.0000
|2025-01-11 09:53:16| train_time: 256.2764 ± 0.0000
|2025-01-11 09:53:17| Flops: 818810880
|2025-01-11 09:53:17| Params: 691925
|2025-01-11 09:53:17| Inference time: 0.33 ms
|2025-01-11 09:53:17| ********************Experiment Success********************
```

