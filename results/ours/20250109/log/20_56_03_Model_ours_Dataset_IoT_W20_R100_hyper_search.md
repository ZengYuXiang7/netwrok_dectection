```python
|2025-01-09 20:56:03| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c6a25353050>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 100,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 20:56:03| ********************Experiment Start********************
|2025-01-09 21:01:07| Round=1 BestEpoch=112 Acc=0.9062 F1=0.8574 Precision=0.8575 Recall=0.8582 Training_time=207.4 s 

|2025-01-09 21:01:07| ********************Experiment Results:********************
|2025-01-09 21:01:07| Acc: 0.9062 ± 0.0000
|2025-01-09 21:01:07| F1: 0.8574 ± 0.0000
|2025-01-09 21:01:07| P: 0.8575 ± 0.0000
|2025-01-09 21:01:07| Recall: 0.8582 ± 0.0000
|2025-01-09 21:01:07| train_time: 207.3756 ± 0.0000
|2025-01-09 21:01:08| Flops: 502099200
|2025-01-09 21:01:08| Params: 423221
|2025-01-09 21:01:08| Inference time: 0.37 ms
|2025-01-09 21:01:09| ********************Experiment Success********************
```

