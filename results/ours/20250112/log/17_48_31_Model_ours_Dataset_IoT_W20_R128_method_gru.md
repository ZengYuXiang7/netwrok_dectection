```python
|2025-01-12 17:48:31| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x10cbd6e52420>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-12 17:48:31| ********************Experiment Start********************
|2025-01-12 17:48:33| Acc=0.9246 F1=0.8863 Precision=0.8892 Recall=0.8843 time=312.8 s 
|2025-01-12 17:48:33| ********************Experiment Results:********************
|2025-01-12 17:48:33| Acc: 0.9246 ± 0.0000
|2025-01-12 17:48:33| F1: 0.8863 ± 0.0000
|2025-01-12 17:48:33| P: 0.8892 ± 0.0000
|2025-01-12 17:48:33| Recall: 0.8843 ± 0.0000
|2025-01-12 17:48:33| train_time: 312.8104 ± 0.0000
|2025-01-12 17:48:35| Skip the efficiency calculation
|2025-01-12 17:48:35| ********************Experiment Success********************
```

