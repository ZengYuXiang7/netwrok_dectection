```python
|2025-01-12 23:58:19| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d860cebd580>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 7, 'verbose': 10,
}
|2025-01-12 23:58:19| ********************Experiment Start********************
|2025-01-13 00:06:39| Round=1 BestEpoch= 82 Acc=0.9255 F1=0.8853 Precision=0.8852 Recall=0.8860 Training_time=329.4 s 

|2025-01-13 00:06:39| ********************Experiment Results:********************
|2025-01-13 00:06:39| Acc: 0.9255 ± 0.0000
|2025-01-13 00:06:39| F1: 0.8853 ± 0.0000
|2025-01-13 00:06:39| P: 0.8852 ± 0.0000
|2025-01-13 00:06:39| Recall: 0.8860 ± 0.0000
|2025-01-13 00:06:39| train_time: 329.3617 ± 0.0000
|2025-01-13 00:06:39| Skip the efficiency calculation
|2025-01-13 00:06:40| ********************Experiment Success********************
```

