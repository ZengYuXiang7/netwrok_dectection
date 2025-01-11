```python
|2025-01-09 18:04:38| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x70b94572c9e0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': lstm, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 100,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 18:04:38| ********************Experiment Start********************
|2025-01-09 18:07:54| Round=1 BestEpoch=105 Acc=0.8767 F1=0.8196 Precision=0.8244 Recall=0.8162 Training_time=125.8 s 

|2025-01-09 18:07:54| ********************Experiment Results:********************
|2025-01-09 18:07:54| Acc: 0.8767 ± 0.0000
|2025-01-09 18:07:54| F1: 0.8196 ± 0.0000
|2025-01-09 18:07:54| P: 0.8244 ± 0.0000
|2025-01-09 18:07:54| Recall: 0.8162 ± 0.0000
|2025-01-09 18:07:54| train_time: 125.7835 ± 0.0000
|2025-01-09 18:07:55| Flops: 321792000
|2025-01-09 18:07:55| Params: 164021
|2025-01-09 18:07:55| Inference time: 0.07 ms
|2025-01-09 18:07:56| ********************Experiment Success********************
```

