```python
|2025-01-11 14:40:43| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b96bedaa000>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 128, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': gru, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 14:40:43| ********************Experiment Start********************
|2025-01-11 14:47:54| Round=1 BestEpoch= 93 Acc=0.9197 F1=0.8766 Precision=0.8754 Recall=0.8784 Training_time=283.1 s 

|2025-01-11 14:47:54| ********************Experiment Results:********************
|2025-01-11 14:47:54| Acc: 0.9197 ± 0.0000
|2025-01-11 14:47:54| F1: 0.8766 ± 0.0000
|2025-01-11 14:47:54| P: 0.8754 ± 0.0000
|2025-01-11 14:47:54| Recall: 0.8784 ± 0.0000
|2025-01-11 14:47:54| train_time: 283.1455 ± 0.0000
|2025-01-11 14:47:54| Skip the efficiency calculation
|2025-01-11 14:47:55| ********************Experiment Success********************
```

