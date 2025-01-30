```python
|2025-01-19 05:26:00| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gin, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7380a16fd580>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 05:26:00| ********************Experiment Start********************
|2025-01-19 05:35:33| Round=1 BestEpoch=202 Acc=0.8323 F1=0.7471 Precision=0.7648 Recall=0.7411 Training_time=407.0 s 

|2025-01-19 05:35:33| ********************Experiment Results:********************
|2025-01-19 05:35:33| Acc: 0.8323 ± 0.0000
|2025-01-19 05:35:33| F1: 0.7471 ± 0.0000
|2025-01-19 05:35:33| P: 0.7648 ± 0.0000
|2025-01-19 05:35:33| Recall: 0.7411 ± 0.0000
|2025-01-19 05:35:33| train_time: 407.0141 ± 0.0000
|2025-01-19 05:35:48| Flops: 7296000
|2025-01-19 05:35:48| Params: 34271
|2025-01-19 05:35:48| Inference time: 0.29 ms
|2025-01-19 05:35:48| ********************Experiment Success********************
```

