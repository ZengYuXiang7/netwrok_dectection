```python
|2025-01-14 15:20:24| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7ad30170a420>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 4, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 15:20:24| ********************Experiment Start********************
|2025-01-14 15:33:04| Round=1 BestEpoch=111 Acc=0.9254 F1=0.8870 Precision=0.8861 Recall=0.8884 Training_time=545.8 s 

|2025-01-14 15:33:04| ********************Experiment Results:********************
|2025-01-14 15:33:04| Acc: 0.9254 ± 0.0000
|2025-01-14 15:33:04| F1: 0.8870 ± 0.0000
|2025-01-14 15:33:04| P: 0.8861 ± 0.0000
|2025-01-14 15:33:04| Recall: 0.8884 ± 0.0000
|2025-01-14 15:33:04| train_time: 545.7659 ± 0.0000
|2025-01-14 15:33:04| Flops: 5829169152
|2025-01-14 15:33:04| Params: 2603093
|2025-01-14 15:33:04| Inference time: 0.68 ms
|2025-01-14 15:33:05| ********************Experiment Success********************
```

