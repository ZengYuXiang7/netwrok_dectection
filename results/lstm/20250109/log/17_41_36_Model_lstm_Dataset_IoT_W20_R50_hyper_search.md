```python
|2025-01-09 17:41:36| {
     'Ablation': 0, 'bs': 128, 'classification': True, 'dataset': IoT,
     'debug': False, 'decay': 0.0001, 'density': 0.8, 'device': cuda,
     'epochs': 500, 'eval_set': True, 'experiment': False, 'flow_length_limit': 20,
     'hyper_search': True, 'log': <utils.logger.Logger object at 0x78a07270c860>, 'logger': None, 'loss_func': CrossEntropyLoss,
     'lr': 0.001, 'model': lstm, 'num_classes': 6, 'optim': AdamW,
     'path': ./datasets/, 'patience': 30, 'program_test': False, 'rank': 50,
     'record': True, 'retrain': False, 'rounds': 1, 'seed': 0,
     'time_interval': 10, 'train_size': 500, 'verbose': 10,
}
|2025-01-09 17:41:36| ********************Experiment Start********************
|2025-01-09 17:50:18| Round=1 BestEpoch=335 Acc=0.8682 F1=0.8052 Precision=0.8114 Recall=0.8038 Training_time=394.8 s 

|2025-01-09 17:50:18| ********************Experiment Results:********************
|2025-01-09 17:50:18| Acc: 0.8682 ± 0.0000
|2025-01-09 17:50:18| F1: 0.8052 ± 0.0000
|2025-01-09 17:50:18| P: 0.8114 ± 0.0000
|2025-01-09 17:50:18| Recall: 0.8038 ± 0.0000
|2025-01-09 17:50:18| train_time: 394.8285 ± 0.0000
|2025-01-09 17:50:19| Flops: 84096000
|2025-01-09 17:50:19| Params: 52021
|2025-01-09 17:50:19| Inference time: 0.07 ms
|2025-01-09 17:50:19| ********************Experiment Success********************
```

