```python
|2025-01-20 07:26:14| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c2375bafe60>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 4, 'num_classes': 21, 'num_layers': 3, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 52,
     'record': True, 'retrain': True, 'rounds': 5, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 07:26:14| ********************Experiment Start********************
|2025-01-20 07:40:16| Round=1 BestEpoch=125 Acc=0.9242 F1=0.8710 Precision=0.8753 Recall=0.8679 Training_time=652.0 s 

|2025-01-20 07:55:30| Round=2 BestEpoch=137 Acc=0.9040 F1=0.8512 Precision=0.8582 Recall=0.8483 Training_time=719.0 s 

|2025-01-20 08:06:32| Round=3 BestEpoch= 91 Acc=0.8928 F1=0.8406 Precision=0.8459 Recall=0.8430 Training_time=477.7 s 

|2025-01-20 08:18:35| Round=4 BestEpoch=102 Acc=0.9211 F1=0.8672 Precision=0.8688 Recall=0.8667 Training_time=536.0 s 

|2025-01-20 08:36:23| Round=5 BestEpoch=165 Acc=0.9134 F1=0.8583 Precision=0.8634 Recall=0.8550 Training_time=866.7 s 

|2025-01-20 08:36:23| ********************Experiment Results:********************
|2025-01-20 08:36:23| Acc: 0.9111 ± 0.0115
|2025-01-20 08:36:23| F1: 0.8577 ± 0.0109
|2025-01-20 08:36:23| P: 0.8623 ± 0.0100
|2025-01-20 08:36:23| Recall: 0.8562 ± 0.0098
|2025-01-20 08:36:23| train_time: 650.2689 ± 137.3955
|2025-01-20 08:36:24| Flops: 1105767936
|2025-01-20 08:36:24| Params: 924633
|2025-01-20 08:36:24| Inference time: 1.56 ms
|2025-01-20 08:36:25| ********************Experiment Success********************
```

