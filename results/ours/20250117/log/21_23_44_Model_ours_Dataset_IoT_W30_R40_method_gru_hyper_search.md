```python
|2025-01-17 21:23:44| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e4b146bfc80>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-17 21:23:44| ********************Experiment Start********************
|2025-01-17 21:38:47| Round=1 BestEpoch= 91 Acc=0.9057 F1=0.8418 Precision=0.8459 Recall=0.8400 Training_time=652.1 s 

|2025-01-17 21:38:47| ********************Experiment Results:********************
|2025-01-17 21:38:47| Acc: 0.9057 ± 0.0000
|2025-01-17 21:38:47| F1: 0.8418 ± 0.0000
|2025-01-17 21:38:47| P: 0.8459 ± 0.0000
|2025-01-17 21:38:47| Recall: 0.8400 ± 0.0000
|2025-01-17 21:38:47| train_time: 652.0785 ± 0.0000
|2025-01-17 21:38:47| Flops: 1191450880
|2025-01-17 21:38:47| Params: 772789
|2025-01-17 21:38:47| Inference time: 1.98 ms
|2025-01-17 21:38:48| ********************Experiment Success********************
```

