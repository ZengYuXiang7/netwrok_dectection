```python
|2025-01-16 19:20:42| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d1e65a839e0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-16 19:20:42| ********************Experiment Start********************
|2025-01-16 19:54:20| Round=1 BestEpoch=128 Acc=0.9261 F1=0.8902 Precision=0.8901 Recall=0.8907 Training_time=1563.4 s 

|2025-01-16 19:54:20| ********************Experiment Results:********************
|2025-01-16 19:54:20| Acc: 0.9261 ± 0.0000
|2025-01-16 19:54:20| F1: 0.8902 ± 0.0000
|2025-01-16 19:54:20| P: 0.8901 ± 0.0000
|2025-01-16 19:54:20| Recall: 0.8907 ± 0.0000
|2025-01-16 19:54:20| train_time: 1563.4068 ± 0.0000
|2025-01-16 19:54:22| Flops: 8543522816
|2025-01-16 19:54:22| Params: 7400789
|2025-01-16 19:54:22| Inference time: 1.95 ms
|2025-01-16 19:54:22| ********************Experiment Success********************
```

