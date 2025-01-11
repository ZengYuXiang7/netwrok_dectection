```python
|2025-01-10 00:49:10| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7894abaed9a0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': self, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 00:49:10| ********************Experiment Start********************
|2025-01-10 00:54:06| Round=1 BestEpoch=123 Acc=0.9029 F1=0.8538 Precision=0.8560 Recall=0.8530 Training_time=203.6 s 

|2025-01-10 00:54:06| ********************Experiment Results:********************
|2025-01-10 00:54:06| Acc: 0.9029 ± 0.0000
|2025-01-10 00:54:06| F1: 0.8538 ± 0.0000
|2025-01-10 00:54:06| P: 0.8560 ± 0.0000
|2025-01-10 00:54:06| Recall: 0.8530 ± 0.0000
|2025-01-10 00:54:06| train_time: 203.5535 ± 0.0000
|2025-01-10 00:54:07| Flops: 35229696
|2025-01-10 00:54:07| Params: 108693
|2025-01-10 00:54:07| Inference time: 0.39 ms
|2025-01-10 00:54:07| ********************Experiment Success********************
```

