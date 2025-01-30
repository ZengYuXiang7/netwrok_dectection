```python
|2025-01-12 17:40:19| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x786f0266ab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-12 17:40:19| ********************Experiment Start********************
|2025-01-12 17:48:27| Round=1 BestEpoch= 73 Acc=0.9271 F1=0.8878 Precision=0.8888 Recall=0.8874 Training_time=312.8 s 

|2025-01-12 17:48:27| ********************Experiment Results:********************
|2025-01-12 17:48:27| Acc: 0.9271 ± 0.0000
|2025-01-12 17:48:27| F1: 0.8878 ± 0.0000
|2025-01-12 17:48:27| P: 0.8888 ± 0.0000
|2025-01-12 17:48:27| Recall: 0.8874 ± 0.0000
|2025-01-12 17:48:27| train_time: 312.8104 ± 0.0000
|2025-01-12 17:48:28| Skip the efficiency calculation
|2025-01-12 17:48:29| ********************Experiment Success********************
```

