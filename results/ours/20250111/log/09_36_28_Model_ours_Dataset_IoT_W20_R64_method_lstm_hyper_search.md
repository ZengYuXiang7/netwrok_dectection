```python
|2025-01-11 09:36:28| {
     'Ablation': 0, 'bidirectional': False, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7ade9462a450>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 6, 'optim': AdamW, 'path': ./datasets/, 'patience': 30,
     'program_test': False, 'rank': 64, 'record': True, 'retrain': True,
     'rounds': 1, 'seed': 0, 'seq_method': lstm, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 09:36:28| ********************Experiment Start********************
|2025-01-11 09:41:26| Round=1 BestEpoch= 99 Acc=0.9098 F1=0.8654 Precision=0.8699 Recall=0.8628 Training_time=199.5 s 

|2025-01-11 09:41:26| ********************Experiment Results:********************
|2025-01-11 09:41:26| Acc: 0.9098 ± 0.0000
|2025-01-11 09:41:26| F1: 0.8654 ± 0.0000
|2025-01-11 09:41:26| P: 0.8699 ± 0.0000
|2025-01-11 09:41:26| Recall: 0.8628 ± 0.0000
|2025-01-11 09:41:26| train_time: 199.4560 ± 0.0000
|2025-01-11 09:41:27| Flops: 208311936
|2025-01-11 09:41:27| Params: 175757
|2025-01-11 09:41:27| Inference time: 0.33 ms
|2025-01-11 09:41:28| ********************Experiment Success********************
```

