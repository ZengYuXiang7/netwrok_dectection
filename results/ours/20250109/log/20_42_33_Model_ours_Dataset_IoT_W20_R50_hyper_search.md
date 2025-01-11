```python
|2025-01-09 20:42:33| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7896b672b680>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 20:42:33| ********************Experiment Start********************
|2025-01-09 20:49:57| Round=1 BestEpoch=183 Acc=0.9087 F1=0.8617 Precision=0.8642 Recall=0.8614 Training_time=330.4 s 

|2025-01-09 20:49:57| ********************Experiment Results:********************
|2025-01-09 20:49:57| Acc: 0.9087 ± 0.0000
|2025-01-09 20:49:57| F1: 0.8617 ± 0.0000
|2025-01-09 20:49:57| P: 0.8642 ± 0.0000
|2025-01-09 20:49:57| Recall: 0.8614 ± 0.0000
|2025-01-09 20:49:57| train_time: 330.4292 ± 0.0000
|2025-01-09 20:49:58| Flops: 128329600
|2025-01-09 20:49:58| Params: 107871
|2025-01-09 20:49:58| Inference time: 0.39 ms
|2025-01-09 20:49:59| ********************Experiment Success********************
```

