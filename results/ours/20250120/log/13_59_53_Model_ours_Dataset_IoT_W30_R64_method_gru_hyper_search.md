```python
|2025-01-20 13:59:53| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x78c4c0c75d90>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 1, 'num_classes': 21, 'num_layers': 1, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 13:59:53| ********************Experiment Start********************
|2025-01-20 14:07:38| Round=1 BestEpoch=140 Acc=0.9241 F1=0.8660 Precision=0.8716 Recall=0.8623 Training_time=318.4 s 

|2025-01-20 14:16:41| Round=2 BestEpoch=171 Acc=0.9198 F1=0.8680 Precision=0.8746 Recall=0.8638 Training_time=391.7 s 

|2025-01-20 14:16:41| ********************Experiment Results:********************
|2025-01-20 14:16:41| Acc: 0.9219 ± 0.0022
|2025-01-20 14:16:41| F1: 0.8670 ± 0.0010
|2025-01-20 14:16:41| P: 0.8731 ± 0.0015
|2025-01-20 14:16:41| Recall: 0.8630 ± 0.0007
|2025-01-20 14:16:41| train_time: 355.0675 ± 36.6788
|2025-01-20 14:16:42| Flops: 565665792
|2025-01-20 14:16:42| Params: 548565
|2025-01-20 14:16:42| Inference time: 0.72 ms
|2025-01-20 14:16:42| ********************Experiment Success********************
```

