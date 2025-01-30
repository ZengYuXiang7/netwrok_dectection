```python
|2025-01-20 00:51:58| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7052bc8fb5f0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 2, 'num_classes': 21, 'num_layers': 1, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': True, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 00:51:58| ********************Experiment Start********************
|2025-01-20 01:00:45| Round=1 BestEpoch=187 Acc=0.9215 F1=0.8659 Precision=0.8690 Recall=0.8639 Training_time=424.2 s 

|2025-01-20 01:09:47| Round=2 BestEpoch=193 Acc=0.9213 F1=0.8691 Precision=0.8770 Recall=0.8668 Training_time=439.0 s 

|2025-01-20 01:14:57| Round=3 BestEpoch= 97 Acc=0.9113 F1=0.8539 Precision=0.8568 Recall=0.8536 Training_time=220.8 s 

|2025-01-20 01:22:12| Round=4 BestEpoch=148 Acc=0.9235 F1=0.8695 Precision=0.8786 Recall=0.8658 Training_time=337.5 s 

|2025-01-20 01:30:07| Round=5 BestEpoch=163 Acc=0.9151 F1=0.8553 Precision=0.8640 Recall=0.8495 Training_time=373.5 s 

|2025-01-20 01:30:07| ********************Experiment Results:********************
|2025-01-20 01:30:07| Acc: 0.9185 ± 0.0046
|2025-01-20 01:30:07| F1: 0.8627 ± 0.0068
|2025-01-20 01:30:07| P: 0.8691 ± 0.0081
|2025-01-20 01:30:07| Recall: 0.8599 ± 0.0070
|2025-01-20 01:30:07| train_time: 359.0259 ± 78.0047
|2025-01-20 01:30:07| Flops: 375737856
|2025-01-20 01:30:07| Params: 363345
|2025-01-20 01:30:07| Inference time: 0.72 ms
|2025-01-20 01:30:08| ********************Experiment Success********************
```

