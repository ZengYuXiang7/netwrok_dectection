```python
|2025-01-19 05:35:50| {
     'Ablation': 0, 'bs': 64, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'graph_encoder': gin, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7434602c5280>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': gnn,
     'num_classes': 21, 'optim': AdamW, 'order': 3, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 60, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'time_interval': 10,
     'train_size': 500, 'try_exp': -1, 'verbose': 10,
}
|2025-01-19 05:35:50| ********************Experiment Start********************
|2025-01-19 05:47:11| Round=1 BestEpoch=246 Acc=0.8405 F1=0.7549 Precision=0.7710 Recall=0.7482 Training_time=495.1 s 

|2025-01-19 05:47:11| ********************Experiment Results:********************
|2025-01-19 05:47:11| Acc: 0.8405 ± 0.0000
|2025-01-19 05:47:11| F1: 0.7549 ± 0.0000
|2025-01-19 05:47:11| P: 0.7710 ± 0.0000
|2025-01-19 05:47:11| Recall: 0.7482 ± 0.0000
|2025-01-19 05:47:11| train_time: 495.0858 ± 0.0000
|2025-01-19 05:47:25| Flops: 9907200
|2025-01-19 05:47:25| Params: 41721
|2025-01-19 05:47:25| Inference time: 0.28 ms
|2025-01-19 05:47:25| ********************Experiment Success********************
```

