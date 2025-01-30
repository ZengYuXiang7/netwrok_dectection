```python
|2025-01-13 19:51:53| {
     'Ablation': 0, 'bidirectional': True, 'bs': 128, 'classification': True,
     'continue_train': False, 'dataset': IoT, 'debug': False, 'decay': 0.0001,
     'density': 0.8, 'device': cuda, 'epochs': 500, 'eval_set': True,
     'experiment': False, 'flow_length_limit': 20, 'hyper_search': True, 'log': <utils.logger.Logger object at 0x7dc06e24ab10>,
     'logger': None, 'loss_func': CrossEntropyLoss, 'lr': 0.001, 'model': ours,
     'num_classes': 21, 'num_layers': 3, 'optim': AdamW, 'path': ./datasets/,
     'patience': 30, 'program_test': False, 'rank': 128, 'record': True,
     'retrain': True, 'rounds': 1, 'seed': 0, 'seq_method': gru,
     'time_interval': 10, 'train_size': 500, 'try_exp': 16, 'verbose': 10,
}
|2025-01-13 19:51:53| ********************Experiment Start********************
|2025-01-13 20:06:10| Round=1 BestEpoch=136 Acc=0.9246 F1=0.8830 Precision=0.8816 Recall=0.8848 Training_time=637.5 s 

|2025-01-13 20:06:10| ********************Experiment Results:********************
|2025-01-13 20:06:10| Acc: 0.9246 ± 0.0000
|2025-01-13 20:06:10| F1: 0.8830 ± 0.0000
|2025-01-13 20:06:10| P: 0.8816 ± 0.0000
|2025-01-13 20:06:10| Recall: 0.8848 ± 0.0000
|2025-01-13 20:06:10| train_time: 637.5063 ± 0.0000
|2025-01-13 20:06:11| Flops: 4387180544
|2025-01-13 20:06:11| Params: 2061397
|2025-01-13 20:06:11| Inference time: 0.80 ms
|2025-01-13 20:06:11| ********************Experiment Success********************
```

