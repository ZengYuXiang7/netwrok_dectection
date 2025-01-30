```python
|2025-01-17 21:01:29| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7aac0a0d24e0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-17 21:01:29| ********************Experiment Start********************
|2025-01-17 21:09:02| Round=1 BestEpoch=164 Acc=0.9077 F1=0.8446 Precision=0.8487 Recall=0.8416 Training_time=357.3 s 

|2025-01-17 21:09:02| ********************Experiment Results:********************
|2025-01-17 21:09:02| Acc: 0.9077 ± 0.0000
|2025-01-17 21:09:02| F1: 0.8446 ± 0.0000
|2025-01-17 21:09:02| P: 0.8487 ± 0.0000
|2025-01-17 21:09:02| Recall: 0.8416 ± 0.0000
|2025-01-17 21:09:02| train_time: 357.3492 ± 0.0000
|2025-01-17 21:09:02| Flops: 1024204800
|2025-01-17 21:09:02| Params: 339825
|2025-01-17 21:09:02| Inference time: 0.56 ms
|2025-01-17 21:09:03| ********************Experiment Success********************
```

