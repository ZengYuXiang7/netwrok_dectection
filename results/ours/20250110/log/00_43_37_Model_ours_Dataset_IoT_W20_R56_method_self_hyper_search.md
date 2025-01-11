```python
|2025-01-10 00:43:37| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x77f165ba2cc0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 56,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': self, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 00:43:37| ********************Experiment Start********************
|2025-01-10 00:49:06| Round=1 BestEpoch=140 Acc=0.9063 F1=0.8607 Precision=0.8644 Recall=0.8589 Training_time=232.6 s 

|2025-01-10 00:49:06| ********************Experiment Results:********************
|2025-01-10 00:49:06| Acc: 0.9063 ± 0.0000
|2025-01-10 00:49:06| F1: 0.8607 ± 0.0000
|2025-01-10 00:49:06| P: 0.8644 ± 0.0000
|2025-01-10 00:49:06| Recall: 0.8589 ± 0.0000
|2025-01-10 00:49:06| train_time: 232.5892 ± 0.0000
|2025-01-10 00:49:07| Flops: 27184640
|2025-01-10 00:49:07| Params: 83685
|2025-01-10 00:49:07| Inference time: 0.39 ms
|2025-01-10 00:49:08| ********************Experiment Success********************
```

