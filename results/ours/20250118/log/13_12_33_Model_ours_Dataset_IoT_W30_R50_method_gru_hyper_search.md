```python
|2025-01-18 13:12:33| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7e3fc67bf440>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 13:12:33| ********************Experiment Start********************
|2025-01-18 13:25:09| Round=1 BestEpoch= 90 Acc=0.9029 F1=0.8369 Precision=0.8430 Recall=0.8342 Training_time=544.6 s 

|2025-01-18 13:25:09| ********************Experiment Results:********************
|2025-01-18 13:25:09| Acc: 0.9029 ± 0.0000
|2025-01-18 13:25:09| F1: 0.8369 ± 0.0000
|2025-01-18 13:25:09| P: 0.8430 ± 0.0000
|2025-01-18 13:25:09| Recall: 0.8342 ± 0.0000
|2025-01-18 13:25:09| train_time: 544.6054 ± 0.0000
|2025-01-18 13:25:09| Flops: 1280499200
|2025-01-18 13:25:09| Params: 1011275
|2025-01-18 13:25:09| Inference time: 1.66 ms
|2025-01-18 13:25:09| ********************Experiment Success********************
```

