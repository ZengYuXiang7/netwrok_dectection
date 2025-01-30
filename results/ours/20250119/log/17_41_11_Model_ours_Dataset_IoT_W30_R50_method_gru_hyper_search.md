```python
|2025-01-19 17:41:11| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x78c13130f710>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-19 17:41:11| ********************Experiment Start********************
|2025-01-19 17:49:23| Round=1 BestEpoch= 68 Acc=0.9139 F1=0.8524 Precision=0.8534 Recall=0.8527 Training_time=326.2 s 

|2025-01-19 17:49:23| ********************Experiment Results:********************
|2025-01-19 17:49:23| Acc: 0.9139 ± 0.0000
|2025-01-19 17:49:23| F1: 0.8524 ± 0.0000
|2025-01-19 17:49:23| P: 0.8534 ± 0.0000
|2025-01-19 17:49:23| Recall: 0.8527 ± 0.0000
|2025-01-19 17:49:23| train_time: 326.2286 ± 0.0000
|2025-01-19 17:49:23| Flops: 1373836800
|2025-01-19 17:49:23| Params: 863175
|2025-01-19 17:49:23| Inference time: 1.40 ms
|2025-01-19 17:49:24| ********************Experiment Success********************
```

