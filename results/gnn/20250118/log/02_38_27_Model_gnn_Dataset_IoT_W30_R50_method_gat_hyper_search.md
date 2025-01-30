```python
|2025-01-18 02:38:27| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gat, 'heads': 2, 'hyper_search': True,
     'log': <utils.logger.Logger object at 0x7303c5b1ab70>, 'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001,
     'model': gnn, 'num_classes': 21, 'optim': AdamW, 'order': 3,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': True, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-18 02:38:27| ********************Experiment Start********************
|2025-01-18 03:23:22| Round=1 BestEpoch=129 Acc=0.8426 F1=0.7607 Precision=0.7810 Recall=0.7520 Training_time=1946.5 s 

|2025-01-18 03:23:22| ********************Experiment Results:********************
|2025-01-18 03:23:22| Acc: 0.8426 ± 0.0000
|2025-01-18 03:23:22| F1: 0.7607 ± 0.0000
|2025-01-18 03:23:22| P: 0.7810 ± 0.0000
|2025-01-18 03:23:22| Recall: 0.7520 ± 0.0000
|2025-01-18 03:23:22| train_time: 1946.4805 ± 0.0000
|2025-01-18 03:23:56| Flops: 32064000
|2025-01-18 03:23:56| Params: 46921
|2025-01-18 03:23:56| Inference time: 3.87 ms
|2025-01-18 03:23:56| ********************Experiment Success********************
```

