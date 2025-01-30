```python
|2025-01-18 14:59:01| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a5077d7a150>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 4, 'verbose': 1,
}
|2025-01-18 14:59:01| ********************Experiment Start********************
|2025-01-18 15:14:02| Round=1 BestEpoch= 86 Acc=0.9023 F1=0.8446 Precision=0.8534 Recall=0.8383 Training_time=643.7 s 

|2025-01-18 15:14:02| ********************Experiment Results:********************
|2025-01-18 15:14:02| Acc: 0.9023 ± 0.0000
|2025-01-18 15:14:02| F1: 0.8446 ± 0.0000
|2025-01-18 15:14:02| P: 0.8534 ± 0.0000
|2025-01-18 15:14:02| Recall: 0.8383 ± 0.0000
|2025-01-18 15:14:02| train_time: 643.7190 ± 0.0000
|2025-01-18 15:14:02| Flops: 1490988800
|2025-01-18 15:14:02| Params: 1245025
|2025-01-18 15:14:02| Inference time: 2.11 ms
|2025-01-18 15:14:02| ********************Experiment Success********************
```

