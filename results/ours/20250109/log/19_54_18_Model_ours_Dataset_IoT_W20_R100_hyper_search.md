```python
|2025-01-09 19:54:18| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x770c0e7c6c60>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 100,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 19:54:18| ********************Experiment Start********************
|2025-01-09 20:03:35| Round=1 BestEpoch=259 Acc=0.8798 F1=0.8229 Precision=0.8281 Recall=0.8199 Training_time=426.9 s 

|2025-01-09 20:03:35| ********************Experiment Results:********************
|2025-01-09 20:03:35| Acc: 0.8798 ± 0.0000
|2025-01-09 20:03:35| F1: 0.8229 ± 0.0000
|2025-01-09 20:03:35| P: 0.8281 ± 0.0000
|2025-01-09 20:03:35| Recall: 0.8199 ± 0.0000
|2025-01-09 20:03:35| train_time: 426.9087 ± 0.0000
|2025-01-09 20:03:39| Flops: 347219200
|2025-01-09 20:03:39| Params: 362821
|2025-01-09 20:03:39| Inference time: 0.27 ms
|2025-01-09 20:03:39| ********************Experiment Success********************
```

