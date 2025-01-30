```python
|2025-01-18 13:30:47| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7f1dae383620>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 13:30:47| ********************Experiment Start********************
|2025-01-18 13:40:08| Round=1 BestEpoch= 79 Acc=0.9069 F1=0.8428 Precision=0.8481 Recall=0.8389 Training_time=389.4 s 

|2025-01-18 13:40:08| ********************Experiment Results:********************
|2025-01-18 13:40:08| Acc: 0.9069 ± 0.0000
|2025-01-18 13:40:08| F1: 0.8428 ± 0.0000
|2025-01-18 13:40:08| P: 0.8481 ± 0.0000
|2025-01-18 13:40:08| Recall: 0.8389 ± 0.0000
|2025-01-18 13:40:08| train_time: 389.3939 ± 0.0000
|2025-01-18 13:40:08| Flops: 937683200
|2025-01-18 13:40:08| Params: 800525
|2025-01-18 13:40:08| Inference time: 1.39 ms
|2025-01-18 13:40:09| ********************Experiment Success********************
```

