```python
|2025-01-14 12:50:06| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x75bb325a29c0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 2, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 3, 'verbose': 10,
}
|2025-01-14 12:50:06| ********************Experiment Start********************
|2025-01-14 13:02:28| Round=1 BestEpoch=121 Acc=0.9223 F1=0.8819 Precision=0.8799 Recall=0.8841 Training_time=535.7 s 

|2025-01-14 13:08:13| Round=2 BestEpoch= 39 Acc=0.9199 F1=0.8713 Precision=0.8762 Recall=0.8676 Training_time=175.4 s 

|2025-01-14 13:08:13| ********************Experiment Results:********************
|2025-01-14 13:08:13| Acc: 0.9211 ± 0.0012
|2025-01-14 13:08:13| F1: 0.8766 ± 0.0053
|2025-01-14 13:08:13| P: 0.8781 ± 0.0019
|2025-01-14 13:08:13| Recall: 0.8758 ± 0.0083
|2025-01-14 13:08:13| train_time: 355.5508 ± 180.1132
|2025-01-14 13:08:14| Flops: 4384100352
|2025-01-14 13:08:14| Params: 2047445
|2025-01-14 13:08:14| Inference time: 0.75 ms
|2025-01-14 13:08:15| ********************Experiment Success********************
```

