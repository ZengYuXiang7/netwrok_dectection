```python
|2025-01-09 17:58:55| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7a55bacffa70>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': lstm, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 80,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 17:58:55| ********************Experiment Start********************
|2025-01-09 18:04:34| Round=1 BestEpoch=205 Acc=0.8735 F1=0.8139 Precision=0.8173 Recall=0.8115 Training_time=243.1 s 

|2025-01-09 18:04:34| ********************Experiment Results:********************
|2025-01-09 18:04:34| Acc: 0.8735 ± 0.0000
|2025-01-09 18:04:34| F1: 0.8139 ± 0.0000
|2025-01-09 18:04:34| P: 0.8173 ± 0.0000
|2025-01-09 18:04:34| Recall: 0.8115 ± 0.0000
|2025-01-09 18:04:34| train_time: 243.1279 ± 0.0000
|2025-01-09 18:04:35| Flops: 208281600
|2025-01-09 18:04:35| Params: 112021
|2025-01-09 18:04:35| Inference time: 0.07 ms
|2025-01-09 18:04:35| ********************Experiment Success********************
```

