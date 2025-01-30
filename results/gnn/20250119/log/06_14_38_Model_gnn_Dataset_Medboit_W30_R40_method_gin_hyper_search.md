```python
|2025-01-19 06:14:38| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': Medboit, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gin, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7dd55260c2f0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 40, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 06:14:38| ********************Experiment Start********************
|2025-01-19 06:16:25| Round=1 BestEpoch=193 Acc=0.7488 F1=0.6863 Precision=0.6958 Recall=0.6796 Training_time=64.3 s 

|2025-01-19 06:16:25| ********************Experiment Results:********************
|2025-01-19 06:16:25| Acc: 0.7488 ± 0.0000
|2025-01-19 06:16:25| F1: 0.6863 ± 0.0000
|2025-01-19 06:16:25| P: 0.6958 ± 0.0000
|2025-01-19 06:16:25| Recall: 0.6796 ± 0.0000
|2025-01-19 06:16:25| train_time: 64.2652 ± 0.0000
|2025-01-19 06:16:26| Flops: 4070400
|2025-01-19 06:16:26| Params: 11408
|2025-01-19 06:16:26| Inference time: 0.29 ms
|2025-01-19 06:16:27| ********************Experiment Success********************
```

