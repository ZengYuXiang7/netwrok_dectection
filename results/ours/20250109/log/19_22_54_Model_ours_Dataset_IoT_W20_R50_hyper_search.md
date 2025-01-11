```python
|2025-01-09 19:22:54| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x736266015820>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 19:22:54| ********************Experiment Start********************
|2025-01-09 19:33:44| Round=1 BestEpoch=320 Acc=0.8828 F1=0.8239 Precision=0.8285 Recall=0.8227 Training_time=506.4 s 

|2025-01-09 19:33:44| ********************Experiment Results:********************
|2025-01-09 19:33:44| Acc: 0.8828 ± 0.0000
|2025-01-09 19:33:44| F1: 0.8239 ± 0.0000
|2025-01-09 19:33:44| P: 0.8285 ± 0.0000
|2025-01-09 19:33:44| Recall: 0.8227 ± 0.0000
|2025-01-09 19:33:44| train_time: 506.4487 ± 0.0000
|2025-01-09 19:33:44| Flops: 89289600
|2025-01-09 19:33:44| Params: 92671
|2025-01-09 19:33:44| Inference time: 0.28 ms
|2025-01-09 19:33:45| ********************Experiment Success********************
```

