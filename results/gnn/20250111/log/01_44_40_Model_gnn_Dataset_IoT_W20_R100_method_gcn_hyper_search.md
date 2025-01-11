```python
|2025-01-11 01:44:40| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x77a9957faba0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 6, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 100, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'verbose': 10,
}
|2025-01-11 01:44:40| ********************Experiment Start********************
|2025-01-11 02:26:13| Round=1 BestEpoch=321 Acc=0.8543 F1=0.7858 Precision=0.7987 Recall=0.7767 Training_time=1983.2 s 

|2025-01-11 02:26:13| ********************Experiment Results:********************
|2025-01-11 02:26:13| Acc: 0.8543 ± 0.0000
|2025-01-11 02:26:13| F1: 0.7858 ± 0.0000
|2025-01-11 02:26:13| P: 0.7987 ± 0.0000
|2025-01-11 02:26:13| Recall: 0.7767 ± 0.0000
|2025-01-11 02:26:13| train_time: 1983.2094 ± 0.0000
|2025-01-11 02:26:37| Flops: 4352000
|2025-01-11 02:26:37| Params: 42821
|2025-01-11 02:26:37| Inference time: 1.22 ms
|2025-01-11 02:26:38| ********************Experiment Success********************
```

