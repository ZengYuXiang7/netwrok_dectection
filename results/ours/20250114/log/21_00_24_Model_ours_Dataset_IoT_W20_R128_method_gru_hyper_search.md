```python
|2025-01-14 21:00:24| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x72694ff8a420>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 21:00:24| ********************Experiment Start********************
|2025-01-14 21:23:42| Round=1 BestEpoch=158 Acc=0.9192 F1=0.8773 Precision=0.8777 Recall=0.8773 Training_time=1100.5 s 

|2025-01-14 21:23:42| ********************Experiment Results:********************
|2025-01-14 21:23:42| Acc: 0.9192 ± 0.0000
|2025-01-14 21:23:42| F1: 0.8773 ± 0.0000
|2025-01-14 21:23:42| P: 0.8777 ± 0.0000
|2025-01-14 21:23:42| Recall: 0.8773 ± 0.0000
|2025-01-14 21:23:42| train_time: 1100.5407 ± 0.0000
|2025-01-14 21:23:43| Flops: 8762822656
|2025-01-14 21:23:43| Params: 4052949
|2025-01-14 21:23:43| Inference time: 1.13 ms
|2025-01-14 21:23:44| ********************Experiment Success********************
```

