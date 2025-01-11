```python
|2025-01-09 23:10:14| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x72a4c831aa50>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': lstm, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:10:14| ********************Experiment Start********************
|2025-01-09 23:13:02| Round=1 BestEpoch= 56 Acc=0.8546 F1=0.8074 Precision=0.8136 Recall=0.8116 Training_time=94.0 s 

|2025-01-09 23:13:02| ********************Experiment Results:********************
|2025-01-09 23:13:02| Acc: 0.8546 ± 0.0000
|2025-01-09 23:13:02| F1: 0.8074 ± 0.0000
|2025-01-09 23:13:02| P: 0.8136 ± 0.0000
|2025-01-09 23:13:02| Recall: 0.8116 ± 0.0000
|2025-01-09 23:13:02| train_time: 93.9606 ± 0.0000
|2025-01-09 23:13:03| Flops: 208244736
|2025-01-09 23:13:03| Params: 175253
|2025-01-09 23:13:03| Inference time: 0.35 ms
|2025-01-09 23:13:04| ********************Experiment Success********************
```

