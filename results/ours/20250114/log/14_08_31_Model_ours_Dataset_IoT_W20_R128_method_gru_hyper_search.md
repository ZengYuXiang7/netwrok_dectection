```python
|2025-01-14 14:08:31| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x716adbb743e0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 10,
}
|2025-01-14 14:08:31| ********************Experiment Start********************
|2025-01-14 14:16:54| Round=1 BestEpoch= 73 Acc=0.9234 F1=0.8814 Precision=0.8795 Recall=0.8838 Training_time=319.0 s 

|2025-01-14 14:16:54| ********************Experiment Results:********************
|2025-01-14 14:16:54| Acc: 0.9234 ± 0.0000
|2025-01-14 14:16:54| F1: 0.8814 ± 0.0000
|2025-01-14 14:16:54| P: 0.8795 ± 0.0000
|2025-01-14 14:16:54| Recall: 0.8838 ± 0.0000
|2025-01-14 14:16:54| train_time: 319.0285 ± 0.0000
|2025-01-14 14:16:55| Flops: 4384100352
|2025-01-14 14:16:55| Params: 2047445
|2025-01-14 14:16:55| Inference time: 0.69 ms
|2025-01-14 14:16:55| ********************Experiment Success********************
```

