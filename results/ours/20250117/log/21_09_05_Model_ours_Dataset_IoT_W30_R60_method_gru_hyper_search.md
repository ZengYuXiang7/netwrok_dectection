```python
|2025-01-17 21:09:05| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x70b0eabaecc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 60, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-17 21:09:05| ********************Experiment Start********************
|2025-01-17 21:12:02| Round=1 BestEpoch= 46 Acc=0.9016 F1=0.8406 Precision=0.8464 Recall=0.8383 Training_time=99.8 s 

|2025-01-17 21:12:02| ********************Experiment Results:********************
|2025-01-17 21:12:02| Acc: 0.9016 ± 0.0000
|2025-01-17 21:12:02| F1: 0.8406 ± 0.0000
|2025-01-17 21:12:02| P: 0.8464 ± 0.0000
|2025-01-17 21:12:02| Recall: 0.8383 ± 0.0000
|2025-01-17 21:12:02| train_time: 99.8282 ± 0.0000
|2025-01-17 21:12:02| Flops: 1466459520
|2025-01-17 21:12:02| Params: 487785
|2025-01-17 21:12:02| Inference time: 0.54 ms
|2025-01-17 21:12:03| ********************Experiment Success********************
```

