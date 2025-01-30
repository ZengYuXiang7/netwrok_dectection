```python
|2025-01-19 03:46:33| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7d12363becc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 60, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 03:46:33| ********************Experiment Start********************
|2025-01-19 04:05:02| Round=1 BestEpoch=259 Acc=0.8736 F1=0.8053 Precision=0.8102 Recall=0.8032 Training_time=857.2 s 

|2025-01-19 04:05:02| ********************Experiment Results:********************
|2025-01-19 04:05:02| Acc: 0.8736 ± 0.0000
|2025-01-19 04:05:02| F1: 0.8053 ± 0.0000
|2025-01-19 04:05:02| P: 0.8102 ± 0.0000
|2025-01-19 04:05:02| Recall: 0.8032 ± 0.0000
|2025-01-19 04:05:02| train_time: 857.2219 ± 0.0000
|2025-01-19 04:05:17| Flops: 3916800
|2025-01-19 04:05:17| Params: 38301
|2025-01-19 04:05:17| Inference time: 1.18 ms
|2025-01-19 04:05:18| ********************Experiment Success********************
```

