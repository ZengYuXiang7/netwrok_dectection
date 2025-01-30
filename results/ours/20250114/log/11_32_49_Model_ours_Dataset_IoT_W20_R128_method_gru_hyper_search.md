```python
|2025-01-14 11:32:49| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7493f4f38920>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 16, 'verbose': 10,
}
|2025-01-14 11:32:49| ********************Experiment Start********************
|2025-01-14 11:47:18| Round=1 BestEpoch=149 Acc=0.9271 F1=0.8887 Precision=0.8875 Recall=0.8904 Training_time=651.6 s 

|2025-01-14 11:47:18| ********************Experiment Results:********************
|2025-01-14 11:47:18| Acc: 0.9271 ± 0.0000
|2025-01-14 11:47:18| F1: 0.8887 ± 0.0000
|2025-01-14 11:47:18| P: 0.8875 ± 0.0000
|2025-01-14 11:47:18| Recall: 0.8904 ± 0.0000
|2025-01-14 11:47:18| train_time: 651.5889 ± 0.0000
|2025-01-14 11:47:19| Flops: 4383772672
|2025-01-14 11:47:19| Params: 2044757
|2025-01-14 11:47:19| Inference time: 0.68 ms
|2025-01-14 11:47:19| ********************Experiment Success********************
```

