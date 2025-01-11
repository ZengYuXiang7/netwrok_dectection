```python
|2025-01-09 23:13:06| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7b0013a07500>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 104,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': lstm, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:13:06| ********************Experiment Start********************
|2025-01-09 23:16:39| Round=1 BestEpoch= 76 Acc=0.8823 F1=0.8344 Precision=0.8334 Recall=0.8377 Training_time=130.9 s 

|2025-01-09 23:16:39| ********************Experiment Results:********************
|2025-01-09 23:16:39| Acc: 0.8823 ± 0.0000
|2025-01-09 23:16:39| F1: 0.8344 ± 0.0000
|2025-01-09 23:16:39| P: 0.8334 ± 0.0000
|2025-01-09 23:16:39| Recall: 0.8377 ± 0.0000
|2025-01-09 23:16:39| train_time: 130.9492 ± 0.0000
|2025-01-09 23:16:39| Flops: 542603776
|2025-01-09 23:16:39| Params: 457413
|2025-01-09 23:16:39| Inference time: 0.35 ms
|2025-01-09 23:16:40| ********************Experiment Success********************
```

