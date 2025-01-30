```python
|2025-01-19 02:47:08| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'continue_train': False,
     'dataset': IoT, 'debug': False, 'decay': 0.0001, 'density': 0.8,
     'device': cuda, 'epochs': 500, 'eval_set': True, 'experiment': False,
     'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7abcce7cc6b0>, 'logger': None,
     'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': lstm, 'num_classes': 21,
     'optim': AdamW, 'path': ./datasets/, 'patience': 30, 'program_test': False,
     'rank': 50, 'record': True, 'retrain': True, 'rounds': 1,
     'seed': 0, 'time_interval': 10, 'train_size': 500, 'try_exp': -1,
     'verbose': 10,
}
|2025-01-19 02:47:08| ********************Experiment Start********************
|2025-01-19 02:49:25| Round=1 BestEpoch=143 Acc=0.8918 F1=0.8296 Precision=0.8329 Recall=0.8280 Training_time=92.9 s 

|2025-01-19 02:49:25| ********************Experiment Results:********************
|2025-01-19 02:49:25| Acc: 0.8918 ± 0.0000
|2025-01-19 02:49:25| F1: 0.8296 ± 0.0000
|2025-01-19 02:49:25| P: 0.8329 ± 0.0000
|2025-01-19 02:49:25| Recall: 0.8280 ± 0.0000
|2025-01-19 02:49:25| train_time: 92.9283 ± 0.0000
|2025-01-19 02:49:25| Flops: 126144000
|2025-01-19 02:49:25| Params: 62521
|2025-01-19 02:49:25| Inference time: 0.07 ms
|2025-01-19 02:49:26| ********************Experiment Success********************
```

