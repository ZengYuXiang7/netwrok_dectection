```python
|2025-01-12 09:43:41| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x76d62e2becc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-12 09:43:41| ********************Experiment Start********************
|2025-01-12 09:53:10| Round=1 BestEpoch= 81 Acc=0.9254 F1=0.8867 Precision=0.8848 Recall=0.8890 Training_time=374.8 s 

|2025-01-12 09:53:10| ********************Experiment Results:********************
|2025-01-12 09:53:10| Acc: 0.9254 ± 0.0000
|2025-01-12 09:53:10| F1: 0.8867 ± 0.0000
|2025-01-12 09:53:10| P: 0.8848 ± 0.0000
|2025-01-12 09:53:10| Recall: 0.8890 ± 0.0000
|2025-01-12 09:53:10| train_time: 374.8352 ± 0.0000
|2025-01-12 09:53:10| Skip the efficiency calculation
|2025-01-12 09:53:11| ********************Experiment Success********************
```

