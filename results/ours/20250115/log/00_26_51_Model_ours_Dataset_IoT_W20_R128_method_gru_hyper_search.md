```python
|2025-01-15 00:26:51| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7048324ece60>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-15 00:26:51| ********************Experiment Start********************
|2025-01-15 00:53:06| Round=1 BestEpoch= 96 Acc=0.9264 F1=0.8860 Precision=0.8866 Recall=0.8863 Training_time=1151.8 s 

|2025-01-15 00:53:07| ********************Experiment Results:********************
|2025-01-15 00:53:07| Acc: 0.9264 ± 0.0000
|2025-01-15 00:53:07| F1: 0.8860 ± 0.0000
|2025-01-15 00:53:07| P: 0.8866 ± 0.0000
|2025-01-15 00:53:07| Recall: 0.8863 ± 0.0000
|2025-01-15 00:53:07| train_time: 1151.8225 ± 0.0000
|2025-01-15 00:53:08| Flops: 8549814272
|2025-01-15 00:53:08| Params: 7449941
|2025-01-15 00:53:08| Inference time: 1.97 ms
|2025-01-15 00:53:09| ********************Experiment Success********************
```

