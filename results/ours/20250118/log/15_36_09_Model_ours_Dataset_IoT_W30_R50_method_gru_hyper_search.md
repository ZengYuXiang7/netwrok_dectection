```python
|2025-01-18 15:36:09| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 30, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7403165be750>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 2, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 50, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 7, 'verbose': 1,
}
|2025-01-18 15:36:09| ********************Experiment Start********************
|2025-01-18 15:48:54| Round=1 BestEpoch= 87 Acc=0.9047 F1=0.8352 Precision=0.8457 Recall=0.8322 Training_time=546.9 s 

|2025-01-18 15:48:54| ********************Experiment Results:********************
|2025-01-18 15:48:54| Acc: 0.9047 ± 0.0000
|2025-01-18 15:48:54| F1: 0.8352 ± 0.0000
|2025-01-18 15:48:54| P: 0.8457 ± 0.0000
|2025-01-18 15:48:54| Recall: 0.8322 ± 0.0000
|2025-01-18 15:48:54| train_time: 546.8696 ± 0.0000
|2025-01-18 15:48:55| Flops: 1055795200
|2025-01-18 15:48:55| Params: 1016675
|2025-01-18 15:48:55| Inference time: 1.84 ms
|2025-01-18 15:48:55| ********************Experiment Success********************
```

