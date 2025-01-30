```python
|2025-01-20 08:36:29| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x72f19de99b50>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 1, 'num_classes': 21, 'num_layers': 4, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': True, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 08:36:29| ********************Experiment Start********************
|2025-01-20 09:00:44| Round=1 BestEpoch=181 Acc=0.9224 F1=0.8728 Precision=0.8849 Recall=0.8655 Training_time=1203.9 s 

|2025-01-20 09:39:12| Round=2 BestEpoch=302 Acc=0.8313 F1=0.7994 Precision=0.8361 Recall=0.7791 Training_time=2023.5 s 

|2025-01-20 09:53:41| Round=3 BestEpoch= 95 Acc=0.7991 F1=0.7526 Precision=0.8169 Recall=0.7301 Training_time=636.7 s 

|2025-01-20 10:13:31| Round=4 BestEpoch=141 Acc=0.7389 F1=0.6605 Precision=0.7047 Recall=0.6389 Training_time=945.6 s 

|2025-01-20 10:37:05| Round=5 BestEpoch=173 Acc=0.8328 F1=0.7954 Precision=0.8353 Recall=0.7714 Training_time=1161.9 s 

|2025-01-20 10:37:05| ********************Experiment Results:********************
|2025-01-20 10:37:05| Acc: 0.8249 ± 0.0594
|2025-01-20 10:37:05| F1: 0.7761 ± 0.0696
|2025-01-20 10:37:05| P: 0.8156 ± 0.0598
|2025-01-20 10:37:05| Recall: 0.7570 ± 0.0737
|2025-01-20 10:37:05| train_time: 1194.3099 ± 460.7746
|2025-01-20 10:37:06| Flops: 1470782976
|2025-01-20 10:37:06| Params: 1205277
|2025-01-20 10:37:06| Inference time: 2.01 ms
|2025-01-20 10:37:07| ********************Experiment Success********************
```

