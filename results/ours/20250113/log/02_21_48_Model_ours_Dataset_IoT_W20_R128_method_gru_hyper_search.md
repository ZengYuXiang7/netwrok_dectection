```python
|2025-01-13 02:21:48| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b1567f04200>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 18, 'verbose': 10,
}
|2025-01-13 02:21:48| ********************Experiment Start********************
|2025-01-13 02:25:55| Round=1 BestEpoch= 21 Acc=0.6778 F1=0.5259 Precision=0.5867 Recall=0.5155 Training_time=91.8 s 

|2025-01-13 02:25:55| ********************Experiment Results:********************
|2025-01-13 02:25:55| Acc: 0.6778 ± 0.0000
|2025-01-13 02:25:55| F1: 0.5259 ± 0.0000
|2025-01-13 02:25:55| P: 0.5867 ± 0.0000
|2025-01-13 02:25:55| Recall: 0.5155 ± 0.0000
|2025-01-13 02:25:55| train_time: 91.8003 ± 0.0000
|2025-01-13 02:25:55| Skip the efficiency calculation
|2025-01-13 02:25:56| ********************Experiment Success********************
```

