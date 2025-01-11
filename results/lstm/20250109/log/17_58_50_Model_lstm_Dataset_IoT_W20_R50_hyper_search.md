```python
|2025-01-09 17:58:50| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x751146b7c9b0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': lstm, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 17:58:50| ********************Experiment Start********************
|2025-01-09 17:58:52| Acc=0.8540 F1=0.7837 Precision=0.7919 Recall=0.7789 time=394.8 s 
|2025-01-09 17:58:52| ********************Experiment Results:********************
|2025-01-09 17:58:52| Acc: 0.8540 ± 0.0000
|2025-01-09 17:58:52| F1: 0.7837 ± 0.0000
|2025-01-09 17:58:52| P: 0.7919 ± 0.0000
|2025-01-09 17:58:52| Recall: 0.7789 ± 0.0000
|2025-01-09 17:58:52| train_time: 394.8285 ± 0.0000
|2025-01-09 17:58:53| Flops: 84096000
|2025-01-09 17:58:53| Params: 52021
|2025-01-09 17:58:53| Inference time: 0.09 ms
|2025-01-09 17:58:53| ********************Experiment Success********************
```

