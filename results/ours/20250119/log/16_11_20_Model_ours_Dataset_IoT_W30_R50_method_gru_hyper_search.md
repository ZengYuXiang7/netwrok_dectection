```python
|2025-01-19 16:11:20| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b415b2f5b50>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 16:11:20| ********************Experiment Start********************
|2025-01-19 16:23:27| Round=1 BestEpoch= 91 Acc=0.9145 F1=0.8498 Precision=0.8588 Recall=0.8457 Training_time=525.1 s 

|2025-01-19 16:23:27| ********************Experiment Results:********************
|2025-01-19 16:23:27| Acc: 0.9145 ± 0.0000
|2025-01-19 16:23:27| F1: 0.8498 ± 0.0000
|2025-01-19 16:23:27| P: 0.8588 ± 0.0000
|2025-01-19 16:23:27| Recall: 0.8457 ± 0.0000
|2025-01-19 16:23:27| train_time: 525.1416 ± 0.0000
|2025-01-19 16:23:27| Flops: 1440480000
|2025-01-19 16:23:27| Params: 1028775
|2025-01-19 16:23:27| Inference time: 1.73 ms
|2025-01-19 16:23:28| ********************Experiment Success********************
```

