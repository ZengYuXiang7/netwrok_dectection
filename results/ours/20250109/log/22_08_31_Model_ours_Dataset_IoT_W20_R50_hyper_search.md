```python
|2025-01-09 22:08:31| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7401194f6150>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 22:08:31| ********************Experiment Start********************
|2025-01-09 22:16:25| Round=1 BestEpoch=199 Acc=0.9044 F1=0.8592 Precision=0.8634 Recall=0.8582 Training_time=355.8 s 

|2025-01-09 22:16:25| ********************Experiment Results:********************
|2025-01-09 22:16:25| Acc: 0.9044 ± 0.0000
|2025-01-09 22:16:25| F1: 0.8592 ± 0.0000
|2025-01-09 22:16:25| P: 0.8634 ± 0.0000
|2025-01-09 22:16:25| Recall: 0.8582 ± 0.0000
|2025-01-09 22:16:25| train_time: 355.8068 ± 0.0000
|2025-01-09 22:16:29| Flops: 21833600
|2025-01-09 22:16:29| Params: 67071
|2025-01-09 22:16:29| Inference time: 0.41 ms
|2025-01-09 22:16:29| ********************Experiment Success********************
```

