```python
|2025-01-09 19:44:52| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x76afecbdecc0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 19:44:52| ********************Experiment Start********************
|2025-01-09 19:44:53| Acc=0.8828 F1=0.8239 Precision=0.8285 Recall=0.8227 time=506.4 s 
|2025-01-09 19:44:53| ********************Experiment Results:********************
|2025-01-09 19:44:53| Acc: 0.8828 ± 0.0000
|2025-01-09 19:44:53| F1: 0.8239 ± 0.0000
|2025-01-09 19:44:53| P: 0.8285 ± 0.0000
|2025-01-09 19:44:53| Recall: 0.8227 ± 0.0000
|2025-01-09 19:44:53| train_time: 506.4487 ± 0.0000
|2025-01-09 19:44:54| Flops: 89289600
|2025-01-09 19:44:54| Params: 92671
|2025-01-09 19:44:54| Inference time: 0.31 ms
|2025-01-09 19:44:54| ********************Experiment Success********************
```

