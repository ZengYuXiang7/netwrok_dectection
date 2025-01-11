```python
|2025-01-10 11:40:56| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': False, 'log': <utils.logger.Logger object at 0xf199e5bb0b0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 56,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'seq_method': gru, 'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-10 11:40:56| ********************Experiment Start********************
|2025-01-10 11:40:57| Acc=0.9100 F1=0.8657 Precision=0.8690 Recall=0.8645 time=255.7 s 
|2025-01-10 11:40:57| ********************Experiment Results:********************
|2025-01-10 11:40:57| Acc: 0.9100 ± 0.0000
|2025-01-10 11:40:57| F1: 0.8657 ± 0.0000
|2025-01-10 11:40:57| P: 0.8690 ± 0.0000
|2025-01-10 11:40:57| Recall: 0.8645 ± 0.0000
|2025-01-10 11:40:57| train_time: 255.6563 ± 0.0000
|2025-01-10 11:40:58| Flops: 127317120
|2025-01-10 11:40:58| Params: 122493
|2025-01-10 11:40:58| Inference time: 0.54 ms
|2025-01-10 11:40:58| ********************Experiment Success********************
```

