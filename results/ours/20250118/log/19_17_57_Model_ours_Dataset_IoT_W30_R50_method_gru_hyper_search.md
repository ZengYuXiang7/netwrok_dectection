```python
|2025-01-18 19:17:57| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x770fa2ececc0>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 4, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 19:17:57| ********************Experiment Start********************
|2025-01-18 19:41:09| Round=1 BestEpoch= 88 Acc=0.9066 F1=0.8445 Precision=0.8554 Recall=0.8373 Training_time=1006.7 s 

|2025-01-18 19:41:09| ********************Experiment Results:********************
|2025-01-18 19:41:09| Acc: 0.9066 ± 0.0000
|2025-01-18 19:41:09| F1: 0.8445 ± 0.0000
|2025-01-18 19:41:09| P: 0.8554 ± 0.0000
|2025-01-18 19:41:09| Recall: 0.8373 ± 0.0000
|2025-01-18 19:41:09| train_time: 1006.6559 ± 0.0000
|2025-01-18 19:41:09| Flops: 2863584000
|2025-01-18 19:41:09| Params: 1924675
|2025-01-18 19:41:09| Inference time: 3.13 ms
|2025-01-18 19:41:10| ********************Experiment Success********************
```

