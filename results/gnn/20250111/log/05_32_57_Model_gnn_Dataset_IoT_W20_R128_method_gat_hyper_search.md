```python
|2025-01-11 05:32:57| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x7e5d47e3cc80>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 6, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 128,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-11 05:32:57| ********************Experiment Start********************
|2025-01-11 06:07:42| Round=1 BestEpoch=191 Acc=0.8899 F1=0.8327 Precision=0.8364 Recall=0.8304 Training_time=1605.5 s 

|2025-01-11 06:07:42| ********************Experiment Results:********************
|2025-01-11 06:07:42| Acc: 0.8899 ± 0.0000
|2025-01-11 06:07:42| F1: 0.8327 ± 0.0000
|2025-01-11 06:07:42| P: 0.8364 ± 0.0000
|2025-01-11 06:07:42| Recall: 0.8304 ± 0.0000
|2025-01-11 06:07:42| train_time: 1605.5470 ± 0.0000
|2025-01-11 06:08:07| Flops: 131399680
|2025-01-11 06:08:07| Params: 153109
|2025-01-11 06:08:07| Inference time: 1.54 ms
|2025-01-11 06:08:08| ********************Experiment Success********************
```

