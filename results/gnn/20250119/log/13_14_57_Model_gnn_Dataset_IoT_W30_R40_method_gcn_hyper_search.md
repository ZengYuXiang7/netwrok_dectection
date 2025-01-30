```python
|2025-01-19 13:14:57| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gcn, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x79cac51dff20>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 13:14:57| ********************Experiment Start********************
|2025-01-19 13:27:40| Round=1 BestEpoch=169 Acc=0.8409 F1=0.7588 Precision=0.7685 Recall=0.7551 Training_time=535.3 s 

|2025-01-19 13:27:40| ********************Experiment Results:********************
|2025-01-19 13:27:40| Acc: 0.8409 ± 0.0000
|2025-01-19 13:27:40| F1: 0.7588 ± 0.0000
|2025-01-19 13:27:40| P: 0.7685 ± 0.0000
|2025-01-19 13:27:40| Recall: 0.7551 ± 0.0000
|2025-01-19 13:27:40| train_time: 535.3316 ± 0.0000
|2025-01-19 13:27:55| Flops: 2611200
|2025-01-19 13:27:55| Params: 25541
|2025-01-19 13:27:55| Inference time: 1.26 ms
|2025-01-19 13:27:56| ********************Experiment Success********************
```

