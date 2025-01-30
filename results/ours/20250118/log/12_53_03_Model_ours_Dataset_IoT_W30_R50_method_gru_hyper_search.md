```python
|2025-01-18 12:53:03| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x773f2c817e90>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 12:53:03| ********************Experiment Start********************
|2025-01-18 13:01:07| Round=1 BestEpoch= 87 Acc=0.8951 F1=0.8313 Precision=0.8354 Recall=0.8293 Training_time=342.0 s 

|2025-01-18 13:01:07| ********************Experiment Results:********************
|2025-01-18 13:01:07| Acc: 0.8951 ± 0.0000
|2025-01-18 13:01:07| F1: 0.8313 ± 0.0000
|2025-01-18 13:01:07| P: 0.8354 ± 0.0000
|2025-01-18 13:01:07| Recall: 0.8293 ± 0.0000
|2025-01-18 13:01:07| train_time: 342.0136 ± 0.0000
|2025-01-18 13:01:07| Flops: 1166227200
|2025-01-18 13:01:07| Params: 652275
|2025-01-18 13:01:07| Inference time: 1.11 ms
|2025-01-18 13:01:07| ********************Experiment Success********************
```

