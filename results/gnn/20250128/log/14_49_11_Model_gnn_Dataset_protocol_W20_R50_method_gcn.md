```python
|2025-01-28 14:49:11| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': protocol, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 20, 'graph_encoder': gcn, 'hyper_search': False, 'log': <utils.logger.Logger object at 0x7bf3469f530>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': False, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-28 14:49:11| ********************Experiment Start********************
|2025-01-28 14:49:52| Round=1 BestEpoch= 78 Ac=0.5866 Pr=0.5351 Rc=0.5270 F1=0.5267 Training_time=15.9 s 

|2025-01-28 14:49:52| ********************Experiment Results:********************
|2025-01-28 14:49:52| AC: 0.5866 ± 0.0000
|2025-01-28 14:49:52| PR: 0.5351 ± 0.0000
|2025-01-28 14:49:52| RC: 0.5270 ± 0.0000
|2025-01-28 14:49:52| F1: 0.5267 ± 0.0000
|2025-01-28 14:49:52| train_time: 15.9435 ± 0.0000
|2025-01-28 14:49:53| Flops: 2560000
|2025-01-28 14:49:53| Params: 27427
|2025-01-28 14:49:53| Inference time: 1.20 ms
|2025-01-28 14:49:53| ********************Experiment Success********************
```

