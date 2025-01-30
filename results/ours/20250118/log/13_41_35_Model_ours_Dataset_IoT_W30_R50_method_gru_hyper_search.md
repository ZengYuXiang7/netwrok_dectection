```python
|2025-01-18 13:41:35| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x783c53fb7530>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 1, 'verbose': 1,
}
|2025-01-18 13:41:35| ********************Experiment Start********************
|2025-01-18 13:51:06| Round=1 BestEpoch=110 Acc=0.9065 F1=0.8433 Precision=0.8510 Recall=0.8413 Training_time=426.8 s 

|2025-01-18 13:51:06| ********************Experiment Results:********************
|2025-01-18 13:51:06| Acc: 0.9065 ± 0.0000
|2025-01-18 13:51:06| F1: 0.8433 ± 0.0000
|2025-01-18 13:51:06| P: 0.8510 ± 0.0000
|2025-01-18 13:51:06| Recall: 0.8413 ± 0.0000
|2025-01-18 13:51:06| train_time: 426.7762 ± 0.0000
|2025-01-18 13:51:07| Flops: 800556800
|2025-01-18 13:51:07| Params: 612275
|2025-01-18 13:51:07| Inference time: 1.10 ms
|2025-01-18 13:51:07| ********************Experiment Success********************
```

