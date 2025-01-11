```python
|2025-01-11 08:44:08| {
     'Ablation': 0, 'bidirectional': False, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7232d526e180>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 64, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': gru, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 08:44:08| ********************Experiment Start********************
|2025-01-11 08:49:51| Round=1 BestEpoch=122 Acc=0.9157 F1=0.8727 Precision=0.8745 Recall=0.8723 Training_time=239.1 s 

|2025-01-11 08:49:51| ********************Experiment Results:********************
|2025-01-11 08:49:51| Acc: 0.9157 ± 0.0000
|2025-01-11 08:49:51| F1: 0.8727 ± 0.0000
|2025-01-11 08:49:51| P: 0.8745 ± 0.0000
|2025-01-11 08:49:51| Recall: 0.8723 ± 0.0000
|2025-01-11 08:49:51| train_time: 239.0577 ± 0.0000
|2025-01-11 08:49:52| Flops: 165385856
|2025-01-11 08:49:52| Params: 159117
|2025-01-11 08:49:52| Inference time: 0.33 ms
|2025-01-11 08:49:53| ********************Experiment Success********************
```

