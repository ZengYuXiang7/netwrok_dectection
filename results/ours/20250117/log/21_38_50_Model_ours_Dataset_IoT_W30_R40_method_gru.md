```python
|2025-01-17 21:38:50| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x82b9280fb00>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-17 21:38:50| ********************Experiment Start********************
|2025-01-17 21:38:51| Acc=0.8994 F1=0.8341 Precision=0.8423 Recall=0.8315 time=652.1 s 
|2025-01-17 21:38:51| ********************Experiment Results:********************
|2025-01-17 21:38:51| Acc: 0.8994 ± 0.0000
|2025-01-17 21:38:51| F1: 0.8341 ± 0.0000
|2025-01-17 21:38:51| P: 0.8423 ± 0.0000
|2025-01-17 21:38:51| Recall: 0.8315 ± 0.0000
|2025-01-17 21:38:51| train_time: 652.0785 ± 0.0000
|2025-01-17 21:38:51| Flops: 1191450880
|2025-01-17 21:38:51| Params: 772789
|2025-01-17 21:38:51| Inference time: 2.52 ms
|2025-01-17 21:38:51| ********************Experiment Success********************
```

