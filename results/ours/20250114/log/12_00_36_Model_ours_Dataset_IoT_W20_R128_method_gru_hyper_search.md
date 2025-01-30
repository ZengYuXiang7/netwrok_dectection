```python
|2025-01-14 12:00:36| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x723cf5c1b860>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 2, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 12:00:36| ********************Experiment Start********************
|2025-01-14 12:06:06| Round=1 BestEpoch= 38 Acc=0.9197 F1=0.8755 Precision=0.8755 Recall=0.8761 Training_time=165.2 s 

|2025-01-14 12:21:02| Round=2 BestEpoch=154 Acc=0.9250 F1=0.8818 Precision=0.8839 Recall=0.8801 Training_time=677.5 s 

|2025-01-14 12:21:02| ********************Experiment Results:********************
|2025-01-14 12:21:02| Acc: 0.9223 ± 0.0026
|2025-01-14 12:21:02| F1: 0.8787 ± 0.0032
|2025-01-14 12:21:02| P: 0.8797 ± 0.0042
|2025-01-14 12:21:02| Recall: 0.8781 ± 0.0020
|2025-01-14 12:21:02| train_time: 421.3476 ± 256.1148
|2025-01-14 12:21:03| Flops: 4384100352
|2025-01-14 12:21:03| Params: 2047445
|2025-01-14 12:21:03| Inference time: 0.66 ms
|2025-01-14 12:21:04| ********************Experiment Success********************
```

