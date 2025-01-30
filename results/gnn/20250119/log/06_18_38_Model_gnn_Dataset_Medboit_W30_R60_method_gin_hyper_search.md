```python
|2025-01-19 06:18:38| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gin, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x72ede94eab70>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 60, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 06:18:38| ********************Experiment Start********************
|2025-01-19 06:20:16| Round=1 BestEpoch=175 Acc=0.7478 F1=0.6834 Precision=0.6925 Recall=0.6761 Training_time=58.4 s 

|2025-01-19 06:20:16| ********************Experiment Results:********************
|2025-01-19 06:20:16| Acc: 0.7478 ± 0.0000
|2025-01-19 06:20:16| F1: 0.6834 ± 0.0000
|2025-01-19 06:20:16| P: 0.6925 ± 0.0000
|2025-01-19 06:20:16| Recall: 0.6761 ± 0.0000
|2025-01-19 06:20:16| train_time: 58.3680 ± 0.0000
|2025-01-19 06:20:17| Flops: 8409600
|2025-01-19 06:20:17| Params: 18308
|2025-01-19 06:20:17| Inference time: 0.28 ms
|2025-01-19 06:20:18| ********************Experiment Success********************
```

