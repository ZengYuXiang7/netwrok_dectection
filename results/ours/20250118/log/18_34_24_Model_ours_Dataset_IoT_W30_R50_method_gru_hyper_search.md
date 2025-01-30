```python
|2025-01-18 18:34:24| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7aaaddb6c3e0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 1, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 18:34:24| ********************Experiment Start********************
|2025-01-18 18:45:42| Round=1 BestEpoch=140 Acc=0.9022 F1=0.8409 Precision=0.8505 Recall=0.8361 Training_time=531.8 s 

|2025-01-18 18:45:42| ********************Experiment Results:********************
|2025-01-18 18:45:42| Acc: 0.9022 ± 0.0000
|2025-01-18 18:45:42| F1: 0.8409 ± 0.0000
|2025-01-18 18:45:42| P: 0.8505 ± 0.0000
|2025-01-18 18:45:42| Recall: 0.8361 ± 0.0000
|2025-01-18 18:45:42| train_time: 531.7815 ± 0.0000
|2025-01-18 18:45:42| Flops: 734688000
|2025-01-18 18:45:42| Params: 626425
|2025-01-18 18:45:42| Inference time: 1.05 ms
|2025-01-18 18:45:43| ********************Experiment Success********************
```

