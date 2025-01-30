```python
|2025-01-29 20:27:11| {
     'ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': ustctfc, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 10, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x108403a8ecc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 52, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-29 20:27:11| ********************Experiment Start********************
|2025-01-29 20:27:58| Round=1 BestEpoch= 81 Ac=0.8504 Pr=0.6653 Rc=0.6839 F1=0.6559 Training_time=20.4 s 

|2025-01-29 20:27:58| ********************Experiment Results:********************
|2025-01-29 20:27:58| AC: 0.8504 ± 0.0000
|2025-01-29 20:27:58| PR: 0.6653 ± 0.0000
|2025-01-29 20:27:58| RC: 0.6839 ± 0.0000
|2025-01-29 20:27:58| F1: 0.6559 ± 0.0000
|2025-01-29 20:27:58| train_time: 20.3633 ± 0.0000
|2025-01-29 20:27:59| Flops: 998400
|2025-01-29 20:27:59| Params: 9273
|2025-01-29 20:27:59| Inference time: 1.28 ms
|2025-01-29 20:27:59| ********************Experiment Success********************
```

