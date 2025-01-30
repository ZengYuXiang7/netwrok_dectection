```python
|2025-01-14 11:19:27| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x79200ca1ef60>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 16, 'verbose': 10,
}
|2025-01-14 11:19:27| ********************Experiment Start********************
|2025-01-14 11:31:38| Round=1 BestEpoch=128 Acc=0.9266 F1=0.8903 Precision=0.8908 Recall=0.8905 Training_time=529.6 s 

|2025-01-14 11:31:38| ********************Experiment Results:********************
|2025-01-14 11:31:38| Acc: 0.9266 ± 0.0000
|2025-01-14 11:31:38| F1: 0.8903 ± 0.0000
|2025-01-14 11:31:38| P: 0.8908 ± 0.0000
|2025-01-14 11:31:38| Recall: 0.8905 ± 0.0000
|2025-01-14 11:31:38| train_time: 529.5856 ± 0.0000
|2025-01-14 11:31:41| Flops: 4385083392
|2025-01-14 11:31:41| Params: 2045013
|2025-01-14 11:31:41| Inference time: 0.68 ms
|2025-01-14 11:31:42| ********************Experiment Success********************
```

