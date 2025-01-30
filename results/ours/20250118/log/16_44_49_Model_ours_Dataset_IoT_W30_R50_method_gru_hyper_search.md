```python
|2025-01-18 16:44:49| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c0a2ddcfaa0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 16:44:49| ********************Experiment Start********************
|2025-01-18 16:54:20| Round=1 BestEpoch= 59 Acc=0.8986 F1=0.8328 Precision=0.8428 Recall=0.8276 Training_time=364.3 s 

|2025-01-18 16:54:20| ********************Experiment Results:********************
|2025-01-18 16:54:20| Acc: 0.8986 ± 0.0000
|2025-01-18 16:54:20| F1: 0.8328 ± 0.0000
|2025-01-18 16:54:20| P: 0.8428 ± 0.0000
|2025-01-18 16:54:20| Recall: 0.8276 ± 0.0000
|2025-01-18 16:54:20| train_time: 364.2757 ± 0.0000
|2025-01-18 16:54:21| Flops: 1440480000
|2025-01-18 16:54:21| Params: 1028775
|2025-01-18 16:54:21| Inference time: 1.76 ms
|2025-01-18 16:54:21| ********************Experiment Success********************
```

