```python
|2025-01-10 00:10:31| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x70d41e421cd0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 56,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': lstm, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 00:10:31| ********************Experiment Start********************
|2025-01-10 00:19:06| Round=1 BestEpoch=227 Acc=0.9060 F1=0.8579 Precision=0.8578 Recall=0.8594 Training_time=393.4 s 

|2025-01-10 00:19:06| ********************Experiment Results:********************
|2025-01-10 00:19:06| Acc: 0.9060 ± 0.0000
|2025-01-10 00:19:06| F1: 0.8579 ± 0.0000
|2025-01-10 00:19:06| P: 0.8578 ± 0.0000
|2025-01-10 00:19:06| Recall: 0.8594 ± 0.0000
|2025-01-10 00:19:06| train_time: 393.4233 ± 0.0000
|2025-01-10 00:19:07| Flops: 160222720
|2025-01-10 00:19:07| Params: 134757
|2025-01-10 00:19:07| Inference time: 0.35 ms
|2025-01-10 00:19:07| ********************Experiment Success********************
```

