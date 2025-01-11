```python
|2025-01-09 21:43:06| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x79ba136ec4d0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 21:43:06| ********************Experiment Start********************
|2025-01-09 21:43:08| Acc=0.8237 F1=0.7664 Precision=0.7754 Recall=0.7684 time=270.9 s 
|2025-01-09 21:43:08| ********************Experiment Results:********************
|2025-01-09 21:43:08| Acc: 0.8237 ± 0.0000
|2025-01-09 21:43:08| F1: 0.7664 ± 0.0000
|2025-01-09 21:43:08| P: 0.7754 ± 0.0000
|2025-01-09 21:43:08| Recall: 0.7684 ± 0.0000
|2025-01-09 21:43:08| train_time: 270.9483 ± 0.0000
|2025-01-09 21:43:09| Flops: 128841600
|2025-01-09 21:43:09| Params: 107971
|2025-01-09 21:43:09| Inference time: 0.47 ms
|2025-01-09 21:43:09| ********************Experiment Success********************
```

