```python
|2025-01-09 19:40:49| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 40,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x7780500f1cd0>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': ours, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 19:40:49| ********************Experiment Start********************
|2025-01-09 19:44:48| Round=1 BestEpoch=211 Acc=0.8100 F1=0.7026 Precision=0.7310 Recall=0.6920 Training_time=165.9 s 

|2025-01-09 19:44:48| ********************Experiment Results:********************
|2025-01-09 19:44:48| Acc: 0.8100 ± 0.0000
|2025-01-09 19:44:48| F1: 0.7026 ± 0.0000
|2025-01-09 19:44:48| P: 0.7310 ± 0.0000
|2025-01-09 19:44:48| Recall: 0.6920 ± 0.0000
|2025-01-09 19:44:48| train_time: 165.9165 ± 0.0000
|2025-01-09 19:44:49| Flops: 177353600
|2025-01-09 19:44:49| Params: 144671
|2025-01-09 19:44:49| Inference time: 0.28 ms
|2025-01-09 19:44:49| ********************Experiment Success********************
```

