```python
|2025-01-20 14:16:44| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x78af7f8efef0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'n_heads': 1, 'num_classes': 21, 'num_layers': 2, 'optim': AdamW,
     'path': ./datasets/, 'patience': 50, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': True, 'rounds': 2, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'try_exp': 1,
     'verbose': 1,
}
|2025-01-20 14:16:44| ********************Experiment Start********************
|2025-01-20 14:35:50| Round=1 BestEpoch=239 Acc=0.9266 F1=0.8758 Precision=0.8816 Recall=0.8714 Training_time=900.5 s 

|2025-01-20 14:51:59| Round=2 BestEpoch=194 Acc=0.9221 F1=0.8731 Precision=0.8767 Recall=0.8701 Training_time=732.2 s 

|2025-01-20 14:51:59| ********************Experiment Results:********************
|2025-01-20 14:51:59| Acc: 0.9243 ± 0.0022
|2025-01-20 14:51:59| F1: 0.8744 ± 0.0014
|2025-01-20 14:51:59| P: 0.8792 ± 0.0024
|2025-01-20 14:51:59| Recall: 0.8707 ± 0.0006
|2025-01-20 14:51:59| train_time: 816.3340 ± 84.1707
|2025-01-20 14:51:59| Flops: 1115185152
|2025-01-20 14:51:59| Params: 972309
|2025-01-20 14:51:59| Inference time: 1.16 ms
|2025-01-20 14:52:00| ********************Experiment Success********************
```

