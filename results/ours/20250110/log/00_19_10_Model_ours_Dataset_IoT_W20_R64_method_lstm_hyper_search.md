```python
|2025-01-10 00:19:10| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7765a7ca38c0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 64,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': lstm, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 00:19:10| ********************Experiment Start********************
|2025-01-10 00:21:58| Round=1 BestEpoch= 56 Acc=0.8546 F1=0.8074 Precision=0.8136 Recall=0.8116 Training_time=93.7 s 

|2025-01-10 00:21:58| ********************Experiment Results:********************
|2025-01-10 00:21:58| Acc: 0.8546 ± 0.0000
|2025-01-10 00:21:58| F1: 0.8074 ± 0.0000
|2025-01-10 00:21:58| P: 0.8136 ± 0.0000
|2025-01-10 00:21:58| Recall: 0.8116 ± 0.0000
|2025-01-10 00:21:58| train_time: 93.7004 ± 0.0000
|2025-01-10 00:21:59| Flops: 208244736
|2025-01-10 00:21:59| Params: 175253
|2025-01-10 00:21:59| Inference time: 0.35 ms
|2025-01-10 00:21:59| ********************Experiment Success********************
```

