```python
|2025-01-11 21:56:23| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e78e6f92b10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 21:56:23| ********************Experiment Start********************
|2025-01-11 22:02:47| Round=1 BestEpoch= 54 Acc=0.9241 F1=0.8852 Precision=0.8872 Recall=0.8844 Training_time=219.2 s 

|2025-01-11 22:02:47| ********************Experiment Results:********************
|2025-01-11 22:02:47| Acc: 0.9241 ± 0.0000
|2025-01-11 22:02:47| F1: 0.8852 ± 0.0000
|2025-01-11 22:02:47| P: 0.8872 ± 0.0000
|2025-01-11 22:02:47| Recall: 0.8844 ± 0.0000
|2025-01-11 22:02:47| train_time: 219.1782 ± 0.0000
|2025-01-11 22:02:48| Skip the efficiency calculation
|2025-01-11 22:02:48| ********************Experiment Success********************
```

