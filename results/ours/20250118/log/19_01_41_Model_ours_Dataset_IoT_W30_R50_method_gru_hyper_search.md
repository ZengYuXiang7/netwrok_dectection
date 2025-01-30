```python
|2025-01-18 19:01:41| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e754bc678f0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 19:01:41| ********************Experiment Start********************
|2025-01-18 19:17:54| Round=1 BestEpoch= 75 Acc=0.9084 F1=0.8498 Precision=0.8608 Recall=0.8428 Training_time=672.5 s 

|2025-01-18 19:17:54| ********************Experiment Results:********************
|2025-01-18 19:17:54| Acc: 0.9084 ± 0.0000
|2025-01-18 19:17:54| F1: 0.8498 ± 0.0000
|2025-01-18 19:17:54| P: 0.8608 ± 0.0000
|2025-01-18 19:17:54| Recall: 0.8428 ± 0.0000
|2025-01-18 19:17:54| train_time: 672.4833 ± 0.0000
|2025-01-18 19:17:55| Flops: 2153952000
|2025-01-18 19:17:55| Params: 1491925
|2025-01-18 19:17:55| Inference time: 2.50 ms
|2025-01-18 19:17:55| ********************Experiment Success********************
```

