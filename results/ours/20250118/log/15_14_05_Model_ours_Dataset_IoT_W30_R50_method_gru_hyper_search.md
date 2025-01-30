```python
|2025-01-18 15:14:05| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x763d52ffa780>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 5, 'verbose': 1,
}
|2025-01-18 15:14:05| ********************Experiment Start********************
|2025-01-18 15:26:13| Round=1 BestEpoch= 81 Acc=0.9065 F1=0.8501 Precision=0.8578 Recall=0.8459 Training_time=510.7 s 

|2025-01-18 15:26:13| ********************Experiment Results:********************
|2025-01-18 15:26:13| Acc: 0.9065 ± 0.0000
|2025-01-18 15:26:13| F1: 0.8501 ± 0.0000
|2025-01-18 15:26:13| P: 0.8578 ± 0.0000
|2025-01-18 15:26:13| Recall: 0.8459 ± 0.0000
|2025-01-18 15:26:13| train_time: 510.6723 ± 0.0000
|2025-01-18 15:26:13| Flops: 1170067200
|2025-01-18 15:26:13| Params: 1029175
|2025-01-18 15:26:13| Inference time: 1.79 ms
|2025-01-18 15:26:14| ********************Experiment Success********************
```

