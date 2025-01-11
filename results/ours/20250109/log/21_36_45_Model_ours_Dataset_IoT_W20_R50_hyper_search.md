```python
|2025-01-09 21:36:45| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x72f69b7f1fa0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 21:36:45| ********************Experiment Start********************
|2025-01-09 21:43:02| Round=1 BestEpoch=145 Acc=0.8360 F1=0.7801 Precision=0.7878 Recall=0.7819 Training_time=270.9 s 

|2025-01-09 21:43:02| ********************Experiment Results:********************
|2025-01-09 21:43:02| Acc: 0.8360 ± 0.0000
|2025-01-09 21:43:02| F1: 0.7801 ± 0.0000
|2025-01-09 21:43:02| P: 0.7878 ± 0.0000
|2025-01-09 21:43:02| Recall: 0.7819 ± 0.0000
|2025-01-09 21:43:02| train_time: 270.9483 ± 0.0000
|2025-01-09 21:43:03| Flops: 128841600
|2025-01-09 21:43:03| Params: 107971
|2025-01-09 21:43:03| Inference time: 0.38 ms
|2025-01-09 21:43:04| ********************Experiment Success********************
```

