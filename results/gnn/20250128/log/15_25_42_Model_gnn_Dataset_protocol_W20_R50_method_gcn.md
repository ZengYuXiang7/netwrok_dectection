```python
|2025-01-28 15:25:42| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x143fe05616a0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-28 15:25:42| ********************Experiment Start********************
|2025-01-28 15:26:10| Round=1 BestEpoch= 33 Ac=0.6314 Pr=0.6064 Rc=0.5938 F1=0.5981 Training_time=7.2 s 

|2025-01-28 15:26:10| ********************Experiment Results:********************
|2025-01-28 15:26:10| AC: 0.6314 ± 0.0000
|2025-01-28 15:26:10| PR: 0.6064 ± 0.0000
|2025-01-28 15:26:10| RC: 0.5938 ± 0.0000
|2025-01-28 15:26:10| F1: 0.5981 ± 0.0000
|2025-01-28 15:26:10| train_time: 7.1930 ± 0.0000
|2025-01-28 15:26:11| Flops: 1600000
|2025-01-28 15:26:11| Params: 12412
|2025-01-28 15:26:11| Inference time: 1.27 ms
|2025-01-28 15:26:11| ********************Experiment Success********************
```

