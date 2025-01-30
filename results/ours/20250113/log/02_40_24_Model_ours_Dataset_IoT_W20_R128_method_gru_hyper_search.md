```python
|2025-01-13 02:40:24| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x78c7416e2b10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 20, 'verbose': 10,
}
|2025-01-13 02:40:24| ********************Experiment Start********************
|2025-01-13 02:53:07| Round=1 BestEpoch=193 Acc=0.8015 F1=0.7125 Precision=0.7492 Recall=0.6919 Training_time=569.7 s 

|2025-01-13 02:53:07| ********************Experiment Results:********************
|2025-01-13 02:53:07| Acc: 0.8015 ± 0.0000
|2025-01-13 02:53:07| F1: 0.7125 ± 0.0000
|2025-01-13 02:53:07| P: 0.7492 ± 0.0000
|2025-01-13 02:53:07| Recall: 0.6919 ± 0.0000
|2025-01-13 02:53:07| train_time: 569.6845 ± 0.0000
|2025-01-13 02:53:08| Skip the efficiency calculation
|2025-01-13 02:53:08| ********************Experiment Success********************
```

