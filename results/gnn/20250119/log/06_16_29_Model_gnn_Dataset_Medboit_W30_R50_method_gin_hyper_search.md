```python
|2025-01-19 06:16:29| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gin, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7c64be0d0620>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 06:16:29| ********************Experiment Start********************
|2025-01-19 06:18:34| Round=1 BestEpoch=228 Acc=0.7488 F1=0.6793 Precision=0.7020 Recall=0.6680 Training_time=76.6 s 

|2025-01-19 06:18:34| ********************Experiment Results:********************
|2025-01-19 06:18:34| Acc: 0.7488 ± 0.0000
|2025-01-19 06:18:34| F1: 0.6793 ± 0.0000
|2025-01-19 06:18:34| P: 0.7020 ± 0.0000
|2025-01-19 06:18:34| Recall: 0.6680 ± 0.0000
|2025-01-19 06:18:34| train_time: 76.6299 ± 0.0000
|2025-01-19 06:18:36| Flops: 6048000
|2025-01-19 06:18:36| Params: 14758
|2025-01-19 06:18:36| Inference time: 0.28 ms
|2025-01-19 06:18:36| ********************Experiment Success********************
```

