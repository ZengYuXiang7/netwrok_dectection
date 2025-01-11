```python
|2025-01-09 23:01:37| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d1f0b4fb0b0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 56,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': lstm, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 23:01:37| ********************Experiment Start********************
|2025-01-09 23:10:10| Round=1 BestEpoch=227 Acc=0.9060 F1=0.8579 Precision=0.8578 Recall=0.8594 Training_time=394.0 s 

|2025-01-09 23:10:10| ********************Experiment Results:********************
|2025-01-09 23:10:10| Acc: 0.9060 ± 0.0000
|2025-01-09 23:10:10| F1: 0.8579 ± 0.0000
|2025-01-09 23:10:10| P: 0.8578 ± 0.0000
|2025-01-09 23:10:10| Recall: 0.8594 ± 0.0000
|2025-01-09 23:10:10| train_time: 393.9708 ± 0.0000
|2025-01-09 23:10:11| Flops: 160222720
|2025-01-09 23:10:11| Params: 134757
|2025-01-09 23:10:11| Inference time: 0.36 ms
|2025-01-09 23:10:12| ********************Experiment Success********************
```

