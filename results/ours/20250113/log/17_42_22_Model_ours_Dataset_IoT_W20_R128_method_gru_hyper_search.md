```python
|2025-01-13 17:42:22| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7aa27bd235f0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 16, 'verbose': 10,
}
|2025-01-13 17:42:22| ********************Experiment Start********************
|2025-01-13 17:45:15| Round=1 BestEpoch=  3 Acc=0.2510 F1=0.0205 Precision=0.0635 Recall=0.0484 Training_time=14.6 s 

|2025-01-13 17:45:15| ********************Experiment Results:********************
|2025-01-13 17:45:15| Acc: 0.2510 ± 0.0000
|2025-01-13 17:45:15| F1: 0.0205 ± 0.0000
|2025-01-13 17:45:15| P: 0.0635 ± 0.0000
|2025-01-13 17:45:15| Recall: 0.0484 ± 0.0000
|2025-01-13 17:45:15| train_time: 14.5693 ± 0.0000
|2025-01-13 17:45:15| Flops: 4385083392
|2025-01-13 17:45:15| Params: 2042581
|2025-01-13 17:45:15| Inference time: 0.82 ms
|2025-01-13 17:45:16| ********************Experiment Success********************
```

