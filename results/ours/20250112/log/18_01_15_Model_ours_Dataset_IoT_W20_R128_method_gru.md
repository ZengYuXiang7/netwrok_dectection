```python
|2025-01-12 18:01:15| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x130a3b04ecc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-12 18:01:15| ********************Experiment Start********************
|2025-01-12 18:01:17| Acc=0.9236 F1=0.8859 Precision=0.8871 Recall=0.8853 time=504.6 s 
|2025-01-12 18:01:17| ********************Experiment Results:********************
|2025-01-12 18:01:17| Acc: 0.9236 ± 0.0000
|2025-01-12 18:01:17| F1: 0.8859 ± 0.0000
|2025-01-12 18:01:17| P: 0.8871 ± 0.0000
|2025-01-12 18:01:17| Recall: 0.8853 ± 0.0000
|2025-01-12 18:01:17| train_time: 504.6345 ± 0.0000
|2025-01-12 18:01:18| Skip the efficiency calculation
|2025-01-12 18:01:18| ********************Experiment Success********************
```

